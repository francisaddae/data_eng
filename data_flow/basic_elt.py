import requests as r
import pandas as pd
from prefect import flow, task, get_run_logger


@task
def extract_from_api():
    """
    This function will extract data from the api and transform it into
    a Pandas DataFrame.
    note: USING PREFECT 2.0
    returns: pd.DataFrame or none
    """
    logger = get_run_logger()
    url = "https://api.coincap.io/v2/assets"
    header = {"Content-Type": "application/json", "Accept-Encoding": "deflate"}

    response_data = r.get(url, headers=header)

    print(f"This is the response status code: {response_data.status_code}")

    # Store JSON data in API_Data
    API_Data = response_data.json()

    # Print json data using loop
    logger.info(API_Data.keys())

    for main_key in API_Data.keys():
        if main_key == "data":
            # the data in list of embeded dictionaries
            df = pd.DataFrame.from_dict(API_Data["data"])
    df["timestamp"] = API_Data["timestamp"]
    df = df.convert_dtypes()
    logger.info(df)
    logger.info(df.info())
    logger.info(df.dtypes)

    return df if True else None


@flow(retries=3, retry_delay_seconds=5)
def main_flow_run():
    extract_from_api()


if __name__ == "__main__":
    main_flow_run()
