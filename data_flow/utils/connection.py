from __future__ import annotations

import os

import sqlalchemy


class Postgres:
    def __init__(self):
        self.user = os.environ.get("POSTGRES_USERNAME")
        self.database = os.environ.get("POSTGRES_DATABASE")
        self.host = os.environ.get("POSTGRES_HOSTNAME")
        self.port = os.environ.get("POSTGRES_PORTNUM")
        self.password = os.environ.get("POSTGRES_PASSWORD")

    def postgres_engine(self):
        engine = sqlalchemy.create_engine(f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}")
        return engine

    def postgres_connection(self):
        eng = self.postgres_engine()
        conn = eng.raw_connection()
        return conn

    def close(self):
        if self.postgres_connection():
            self.postgres_connection().close()
        else:
            self.postgres_engine().dispose()


class ClickHouse:
    """ClickHouse Warehouse connection connector"""

    def __init__(self):
        self.user = os.environ.get("CLICKHOUSE_USER")
        self.database = os.environ.get("CLICKHOUSE_DATABASE")
        self.host = os.environ.get("CLICKHOUSE_HOST")
        self.port = int(os.environ.get("CLICKHOUSE_NATIVE_PORT"))
        self.password = os.environ.get("CLICKHOUSE_CRED")

    def clickhouse_engine(self):
        engine = sqlalchemy.create_engine(
            f"clickhouse+http://{self.user}:{self.password}@{self.host}:\
                {self.port}/{self.database}?protocol=https"
        )
        return engine

    def clickhouse_connection(self):
        conn = self.clickhouse_engine()
        conn = conn.raw_connection()
        return conn

    def close(self):
        if self.clickhouse_connection():
            self.clickhouse_connection().close()
        else:
            self.clickhouse_engine().dispose()
