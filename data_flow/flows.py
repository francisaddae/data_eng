from covidELT.extract import covidDataELT
from lemonadeELT.extract import lemonadeFLOW

if __name__ == "__main__":
    lemonadeFLOW()
    covidDataELT()
    # lemonadeFLOW.deploy(
    #     name="LEMONADE_ELT_FLOW",
    #     work_pool_name="my-cicd-workflow",
    #     image="prefecthq/prefect:3-latest",
    #     cron="10 * * * *"
    # )
    # covidDataELT.deploy(
    #     name="COVID_ELT_FLOW",
    #     work_pool_name="my-cicd-workflow",
    #     image="prefecthq/prefect:3-latest",
    #     cron="10 * * * *"
    # )
