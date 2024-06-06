from __future__ import annotations

import json as js
import os

import pandas as pd
import requests as req
from prefect import flow
from prefect import get_run_logger
from prefect import task
from prefect_dbt.cli.commands import DbtCoreOperation
from sqlalchemy import create_engine


@task(name="covid_Data_Extract")
def get_data():
    logger = get_run_logger()

    logger.info("****  Extract Method ****")
    """
    This function extracts data from an API using the url.
    Uses the request library to get the send a get request to the API
    loads the data into a Dataframe through pandas by json loads function.
    Input: None
    Returns: returns a pandas DataFrame which will be loaded into our datalake
    """
    url = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"

    response = req.get(url)

    df = pd.DataFrame(js.loads(response.content))
    logger.info(f"Previewing random 25 records:\n{df.sample(25)}")

    logger.info("**** Method Ended ****")
    return df


@task(name="covid_Data_Load")
def get_load_data(extracted_data):
    """
    Loading data into postgres serving as a datalake.
    This will be used as a source in DBT
    Input: Pandas Table consisting of all the data elements available
    Returns: True if the data landed in the data warehouse else False
    """

    logger = get_run_logger()

    try:
        logger.info("**** Load Method ****")

        # credentials
        user = os.environ.get("POSTGRES_USERNAME")
        database = os.environ.get("POSTGRES_DATABASE")
        password = os.environ.get("POSTGRES_PASSWORD")
        host = os.environ.get("POSTGRES_HOSTNAME")
        port = os.environ.get("POSTGRES_PORTNUM")

        eng = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

        extracted_data.to_sql("covidData", eng)
        logger.info("Table Loaded successfully!!!")

        return True
    except Exception as err:
        logger.info(err)
        return err


@task(name="covid_DBT")
def trigger_dbt_flow(initaiter=False) -> str:
    if initaiter:
        DbtCoreOperation(
            commands=["dbt build -s covid.sql+ -t dev"],
            project_dir="data_modeling",
            profiles_dir="~/.dbt",
        ).run()
        return "yes"
    else:
        return "no"


@flow(name="CovidELT")
def covidDataELT():
    etz = get_data()
    load = get_load_data(etz)
    trigger_dbt_flow(load)


if __name__ == "__main__":
    covidDataELT()
