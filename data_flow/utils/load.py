from connection import ClickHouse
from connection import Postgres
from sqlalchemy.exc import DataError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import OperationalError


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
            engine = Postgres().postgres_engine()
        else:
            # instantiate db connection
            engine = ClickHouse().clickhouse_engine()

    except OperationalError as sql_error:
        raise (f"Cannot connect to DB: {sql_error}")

    try:
        print(f"Loading {table.upper()} data  into {type.upper()} warehouse")
        data.to_sql(table, engine, if_exists=mode, index=False)
        print(f"**** {table.upper()} TABULAR DATA LOADED SUCCESSFULLY!!! ****")

    except OperationalError as sql_error:
        raise (f"Loading {table.upper()} data error: {sql_error}")
    except IntegrityError as integ_error:
        raise (f"Data Integrity Compromised! See underlying data issue. \n Error Message: {integ_error}")
    except DataError as data_error:
        raise (f"Incorrect data type or data_format: {data_error}")
    finally:
        engine.dispose()
