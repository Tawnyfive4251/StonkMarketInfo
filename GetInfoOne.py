from stonks import get_stonk_info,get_financials_macrotrends
import time
import os
import iexfinance
from iexfinance.stocks import Stock
os.environ['IEX_API_VERSION'] = 'v1'
os.environ['IEX_TOKEN'] = 'sk_9cc370ddf50b4d528796eebd65e6ff0b'

class GetOneInfoUSA:
    def __init__(self):
        ticker = ""
    def get_info(self,ticker):
        print(ticker)
        # company = Stock(ticker)
        # stonkprice = 0
        # stonkprice = company.get_price()
        # print(stonkprice)
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

        averages_info = get_financials_macrotrends(ticker)
        averages = averages_info.get_moving_avgs(ticker)
        fiftyavg = averages[0]
        twohundredavg = averages[1]

        golden = False
        if fiftyavg > twohundredavg:
            golden = True



        result = (ticker,stonkprice,stonkROE,stonkoperatingmargin,stonkPB,stonkdebt,stonkPE,stonkyield,fiftyavg,twohundredavg, golden)
        return result
