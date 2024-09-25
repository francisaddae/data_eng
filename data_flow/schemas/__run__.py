import os

import clickhouse_connect

client = clickhouse_connect.get_client(
    host=os.environ.get("CLICKHOUSE_HOST"), user=os.environ.get("CLICKHOUSE_USER"), password=os.environ.get("CLICKHOUSE_CRED"), secure=True
)


def initialize_clickhouse_schema(conn, filename):
    try:
        file = open(os.getcwd() + filename)
        sql_file = file.read()
        file.close()

        sql_commands = sql_file.split(";")
        for command in sql_commands:
            try:
                print("\n" + command + "\n")
                conn.query(command)

            except Exception as e:
                print("Query Error: %s" % e)
    except Exception as e:
        print("File Error Message: %s" % e)


# initialize_clickhouse_schema(client, "/schemas/schema.sql")
