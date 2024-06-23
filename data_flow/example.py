from __future__ import annotations

from prefect import flow
from prefect import get_run_logger
from prefect import task


@task(name="Print Hello")
def print_hello(name):
    logger = get_run_logger()
    msg = f"Hello {name}!"
    logger.info(msg)
    return msg


@flow(name="Hello Flow")
def hello_world(name="world"):
    print_hello(name)


hello_world("Marvin")
