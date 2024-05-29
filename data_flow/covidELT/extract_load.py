import requests as r
import json as js, os
import pandas as pd
import psycopg2 as pg
from sqlalchemy import create_engine
from prefect import task, flow, get_run_logger
from prefect_dbt.cli.commands import DbtCoreOperation



@task(name='covid_Data_Extract')
def get_data():
    logger = get_run_logger()

    logger.info('****  Extract Method ****')
    '''
    This function extracts data from an API using the url.
    Uses the request library to get the send a get request to the API
    loads the data into a Dataframe through pandas by json loads function.
    Input: None
    Returns: returns a pandas DataFrame which will be loaded into our datalake
    '''
    url = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"

    response = r.get(url)

    df = pd.DataFrame(js.loads(response.content))
    logger.info(f"Previewing random 25 records:\n{df.sample(25)}")

    logger.info('**** Method Ended ****')
    return df

@task(name='covid_Data_Load')
def get_load_data(extracted_data):
    """
        Loading data into postgres serving as a datalake. This will be used as a source in DBT

    Args:
        extracted_data (_type_): _description_

    Returns:
        _type_: _description_
    """

    logger = get_run_logger()

    try:
        logger.info('**** Load Method ****')

        #credentials
        user=os.environ.get('POSTGRES_USERNAME')
        database=os.environ.get('POSTGRES_DATABASE')
        password=os.environ.get('POSTGRES_PASSWORD')
        host=os.environ.get('POSTGRES_HOSTNAME')
        port=os.environ.get('POSTGRES_PORTNUM')

        eng = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

        extracted_data.to_sql('covidData', eng)
        logger.info('Table Loaded successfully!!!')

        return True
    except  Exception as err:
        logger.info(err)
        return err


@task(name='covid_DBT')
def trigger_dbt_flow(initaiter=False) -> str:
    if initaiter:
        DbtCoreOperation(
            commands=["dbt build -s covid.sql+ -t dev"],
            project_dir="data_modeling",
            profiles_dir="~/.dbt"
        ).run()
    else:
        return False


@flow(name="CovidELT")
def covidDataELT():
    e = get_data()
    l = get_load_data(e)
    trigger_dbt_flow(l)
if __name__ == "__main__":
    covidDataELT()