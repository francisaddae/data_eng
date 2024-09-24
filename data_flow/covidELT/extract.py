from __future__ import annotations

import json as js

import pandas as pd
import requests as req
from prefect import flow
from prefect import get_run_logger
from prefect import task
from prefect_dbt.cli.commands import DbtCoreOperation
from utils.load import load_data_into_wh


@task(name="covid_Data_Extract")
def get_data():
    """
    This function extracts data from an API using the url.
    Uses the request library to get the send a get request to the API
    loads the data into a Dataframe through pandas by json loads function.
    Input: None
    Returns: returns a pandas DataFrame which will be loaded into our datalake
    """
    logger = get_run_logger()

    logger.info("****  Extract Method Commencing... ****")

    url = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"

    response = req.get(url)

    df = pd.DataFrame(js.loads(response.content))
    logger.info(f"Previewing random 25 records:\n{df.sample(25)}")

    logger.info("**** Extration Method Ended ****")

    return df


@task(name="covid_Data_Load")
def get_load_data(extracted_data):
    """
    Loading data into ClickHouse serving as a datalake.
    This will be used as a source in DBT
    Input: Pandas Table consisting of all the data elements available
    Returns: True if the data landed in the data warehouse else False
    """

    logger = get_run_logger()

    try:
        logger.info("**** Load Method Commencing... ****")
        extracted_data["index"] = range(1, len(extracted_data) + 1)
        load_data_into_wh(extracted_data, "covidData", "DUCKDB")

        logger.info("**** Load Method Ended ****")

        return True
    except Exception as err:
        logger.info(err)
        return err


@task(name="covid_DBT")
def trigger_dbt_flow(initaiter=False) -> str:
    if initaiter:
        DbtCoreOperation(
            commands=["dbt build -s covid.sql+ -t dev"],
            project_dir="/Users/Francis/Desktop/CODE/data_eng/data_modeling",
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
