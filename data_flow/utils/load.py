import os

import sqlalchemy
from sqlalchemy.exc import DataError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import OperationalError

# credentials for LOCAL POSTGRES
user = os.environ.get("POSTGRES_USERNAME")
database = os.environ.get("POSTGRES_DATABASE")
password = os.environ.get("POSTGRES_PASSWORD")
host = os.environ.get("POSTGRES_HOSTNAME")
port = os.environ.get("POSTGRES_PORTNUM")

# crednetials for CLICKHOUSE
user2 = os.environ.get("CLICKHOUSE_USER")
database2 = os.environ.get("CLICKHOUSE_DATABASE")
password2 = os.environ.get("CLICKHOUSE_CRED")
host2 = os.environ.get("CLICKHOUSE_HOST")
port2 = int(os.environ.get("CLICKHOUSE_NATIVE_PORT"))


def load_data_into_wh(data, table, type="POSTGRES", mode="replace"):
    """
    This function takes in a tabular data and loads it to the datawarehouse.The mode of the data depends on
    the data's availabitlity. Types of Mode are:
        fail: Raise a ValueError. --> Invalid table
        replace: Drop the table before inserting new values. --> Fully refreshed table Only
        append: Insert new values to the existing table. --> Batch or Incremental Table's Only

    Args:
        data (pd.DataFrame): Pandas DataFrame containg informational data
        table (str): Name of the table being ingested into the warehouse
        type (str): Name of the warehouse being used. default to local postgres
        mode (str): Type of data mode being used.
    """

    try:
        if type.upper() == "CLICKHOUSE":
            # instantiate db connection
            engine = sqlalchemy.create_engine(f"clickhouse+http://{user2}:{password2}@{host2}:{port2}/{database2}?protocol=https")
        else:
            # instantiate db connection
            engine = sqlalchemy.create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")
        # conn = engine.connect()

    except OperationalError as sql_error:
        raise (f"Cannot connect to DB: {sql_error}")

    try:
        print(f"Loading {table.upper()} data  into {type.upper()} warehouse")
        data.to_sql(table, engine.raw_connection(), if_exists=mode, index=False)
        print(f"**** {table.upper()} TABULAR DATA LOADED SUCCESSFULLY!!! ****")

    except OperationalError as sql_error:
        raise (f"Loading {table.upper()} data error: {sql_error}")
    except IntegrityError as integ_error:
        raise (f"Data Integrity Compromised! See underlying data issue. \n Error Message: {integ_error}")
    except DataError as data_error:
        raise (f"Incorrect data type or data_format: {data_error}")
    finally:
        engine.dispose()
