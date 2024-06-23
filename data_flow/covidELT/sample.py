from __future__ import annotations

import os

import pandas as pd
from sqlalchemy import create_engine


user = os.environ.get("POSTGRES_USERNAME")
database = os.environ.get("POSTGRES_DATABASE")
password = os.environ.get("POSTGRES_PASSWORD")
host = os.environ.get("POSTGRES_HOSTNAME")
port = os.environ.get("POSTGRES_PORTNUM")

eng = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

# Ingesting googlesheets data into postgres database
gsheetid = "1v8bvtD2aSiVgjrwPZDO3F9X6YSzaycevebeHI_l3rew"
sheet_name = "Policies"
gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
policy = pd.read_csv(gsheet_url)
print(policy.dtypes)
print(policy.head())
policy["Created_At"] = pd.to_datetime(policy["Created_At"]).dt.date
policy["Effective_Date"] = pd.to_datetime(policy["Effective_Date"]).dt.date
policy["Canceled_Date"] = pd.to_datetime(policy["Canceled_Date"]).dt.date
policy["Renewal_Date"] = pd.to_datetime(policy["Renewal_Date"]).dt.date
policy["Tier"] = policy["Tier"].astype(float)
policy["Personal_Property_Limit"] = (
    policy["Personal_Property_Limit"].str.replace(",", "").astype(int)
)
policy["Personal_Liability_Limit"] = (
    policy["Personal_Liability_Limit"].str.replace(",", "").astype(int)
)
print(policy.dtypes)
print(policy.head())
policy.columns = map(str.lower, policy.columns)
policy.to_sql("policies", eng, if_exists="replace", index=False)

# Ingesting googlesheets data into postgres database
gsheetid = "1v8bvtD2aSiVgjrwPZDO3F9X6YSzaycevebeHI_l3rew"
sheet_name = "Users"
gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
users = pd.read_csv(gsheet_url)
print(users.head())
print(users.dtypes)
users["Date_of_Birth"] = pd.to_datetime(users["Date_of_Birth"]).dt.date
print(users.dtypes)
users.columns = map(str.lower, users.columns)
users.to_sql("users", eng, if_exists="replace", index=False)


# Ingesting googlesheets data into postgres database
gsheetid = "1v8bvtD2aSiVgjrwPZDO3F9X6YSzaycevebeHI_l3rew"
sheet_name = "Claims"
gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
claims = pd.read_csv(gsheet_url)
print(claims.dtypes)
print(claims.head())
claims["Submitted_At"] = pd.to_datetime(claims["Submitted_At"]).dt.date
claims["Closed_Date"] = pd.to_datetime(claims["Closed_Date"]).dt.date
claims["Paid"] = claims["Paid"].astype(bool)
claims.columns = map(str.lower, claims.columns)
print(users.dtypes)
claims.to_sql("claims", eng, if_exists="replace", index=False)
