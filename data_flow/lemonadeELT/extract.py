import pandas as pd
from prefect import flow
from prefect import get_run_logger
from prefect import task
from utils.connection import Postgres
from utils.load import load_data_into_wh

p = Postgres()


@task(name="Policy_Table")
def collect_policy_table_info(gsheetid):
    # Ingesting googlesheets data into postgres database
    logger = get_run_logger()
    sheet_name = "Policies"
    gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    policy = pd.read_csv(gsheet_url)
    logger.info(policy.dtypes)
    logger.info(policy.head())
    policy["Created_At"] = pd.to_datetime(policy["Created_At"]).dt.date
    policy["Effective_Date"] = pd.to_datetime(policy["Effective_Date"]).dt.date
    policy["Canceled_Date"] = pd.to_datetime(policy["Canceled_Date"]).dt.date
    policy["Renewal_Date"] = pd.to_datetime(policy["Renewal_Date"]).dt.date
    policy["Tier"] = policy["Tier"].astype(float)
    policy["Personal_Property_Limit"] = policy["Personal_Property_Limit"].str.replace(",", "").astype(int)
    policy["Personal_Liability_Limit"] = policy["Personal_Liability_Limit"].str.replace(",", "").astype(int)
    logger.info(policy.dtypes)
    logger.info(policy.head())
    policy.columns = map(str.lower, policy.columns)
    load_data_into_wh(policy, "policies", "DUCKDB")


@task(name="Users_Table")
def collect_users_table_info(gsheetid):
    # Ingesting googlesheets data into postgres database
    logger = get_run_logger()
    sheet_name = "Users"
    gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    users = pd.read_csv(gsheet_url)
    logger.info(users.head())
    logger.info(users.dtypes)
    users["Date_of_Birth"] = pd.to_datetime(users["Date_of_Birth"]).dt.date
    logger.info(users.dtypes)
    users.columns = map(str.lower, users.columns)
    load_data_into_wh(users, "users", "DUCKDB")


@task(name="Claims_Table")
def collect_claims_table_info(gsheetid):
    # Ingesting googlesheets data into postgres database
    logger = get_run_logger()
    sheet_name = "Claims"
    gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    claims = pd.read_csv(gsheet_url)
    logger.info(claims.dtypes)
    logger.info(claims.head())
    claims["Submitted_At"] = pd.to_datetime(claims["Submitted_At"]).dt.date
    claims["Closed_Date"] = pd.to_datetime(claims["Closed_Date"]).dt.date
    claims["Paid"] = claims["Paid"].astype(bool)
    claims.columns = map(str.lower, claims.columns)
    logger.info(claims.dtypes)
    load_data_into_wh(claims, "claims", "DUCKDB")


@flow(name="lemonadeFLOW")
def lemonadeFLOW():
    gsheetid = "1v8bvtD2aSiVgjrwPZDO3F9X6YSzaycevebeHI_l3rew"
    collect_users_table_info(gsheetid)
    collect_claims_table_info(gsheetid)
    collect_policy_table_info(gsheetid)


if __name__ == "__main__":
    lemonadeFLOW()
