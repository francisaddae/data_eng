from data_flow.covidELT.extract import covidDataELT
from data_flow.lemonadeELT.extract import lemonadeFLOW


if __name__ == "__main__":
    lemonadeFLOW()
    covidDataELT()
