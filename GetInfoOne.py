from stonks import get_stonk_info,get_financials_macrotrends
import time


class GetOneInfoUSA:
    def __init__(self):
        ticker = ""
    def get_info(self,ticker):
        stonk_price = get_stonk_info(ticker)
        time.sleep(0.2)

        stonkpricetemp = stonk_price.get_price()
        stonkprice = stonkpricetemp
        print(stonkpricetemp)

        stonk_price = get_financials_macrotrends(ticker)
        stonkpricetemp = stonk_price.get_ROE()
        stonkROE = stonkpricetemp
        print(stonkpricetemp)

        stonkpricetemp = stonk_price.get_operating_margin()
        stonkoperatingmargin = stonkpricetemp
        print(stonkpricetemp)

        stonkpricetemp = stonk_price.get_pbratio()
        stonkPB = stonkpricetemp
        print(stonkpricetemp)
        # print("passing")

        stonk_info = get_financials_macrotrends(ticker)
        stonkdebttemp = stonk_info.get_debt(ticker)
        stonkdebt = stonkdebttemp
        print(stonkdebttemp)
        # print("passing")

        stonk_info = get_financials_macrotrends(ticker)
        stonkPEtemp = stonk_info.get_PE_ratio(ticker)
        stonkPE = stonkPEtemp
        print(stonkPEtemp)
        # print("passing")

        stonk_price = get_financials_macrotrends(ticker)
        stonkyieldtemp = stonk_price.get_yield(ticker)
        stonkyield = stonkpricetemp
        print(stonkyieldtemp)

        result = (ticker,stonkprice,stonkROE,stonkoperatingmargin,stonkPB,stonkdebt,stonkPE,stonkyield)
        return result
