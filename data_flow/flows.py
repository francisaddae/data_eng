from lemonadeELT.extract import collect_claims_table_info
from lemonadeELT.extract import collect_policy_table_info
from lemonadeELT.extract import collect_users_table_info
from prefect import flow


@flow(name="lemonadeFLOW")
def lemonadeFLOW():
    gsheetid = "1v8bvtD2aSiVgjrwPZDO3F9X6YSzaycevebeHI_l3rew"
    collect_users_table_info(gsheetid)
    collect_claims_table_info(gsheetid)
    collect_policy_table_info(gsheetid)


if __name__ == "__main__":
    lemonadeFLOW()
