#Imports
from selenium import webdriver
# import pandas as pd
from bs4 import BeautifulSoup
import lxml
#setting up the webdriver
driver = webdriver.Chrome('C:/Users/Tawny/Documents/chromedriver.exe')

class get_stonk_info:
    def __init__(self, stonk):
        stonkticker = stonk
        url = "https://old.nasdaq.com/symbol/{}".format(stonkticker)
        driver.get(url)

        # print(Name)
        # print(Ticker)
        # print(Price)

    def get_name(self):
        NameSpan = driver.find_element_by_xpath("//div[@class = 'qwidget_pageheader']")
        Name = NameSpan.text
        return Name
    # def get_ticker(self):
    #     # return "bruh"
    #     TickerSpan = driver.find_element_by_xpath("//span[@class = 'symbol-page-header__symbol']")
    #     Ticker = TickerSpan.text
    #     return Ticker
    def get_price(self):
        PriceSpan = driver.find_element_by_xpath("//div[@class = 'qwidget-dollar']")
        Price = PriceSpan.text
        return Price
    def get_yield(self):
        YieldDiv = driver.find_element_by_xpath('//*[@id="left-column-div"]/div[1]/div[2]/div/div[6]/div[2]')
        Yield = YieldDiv.text
        return Yield
    def get_PE_ratio(self):
        PEDiv = driver.find_element_by_xpath('//*[@id="left-column-div"]/div[1]/div[1]/div/div[8]/div[2]')
        PE = PEDiv.text
        return PE

class get_financials_macrotrends():
    #From Macrotrends DB because NASDAQ is incomplete. Run Debt last!
    def __init__(self,stock):
        url = "https://www.macrotrends.net/stocks/charts/{}/general-motors/financial-ratios".format(stock)
        driver.get(url)
    def get_ROE(self):
        ROEDiv = driver.find_element_by_xpath('//*[@id="row13jqxgrid"]/div[3]/div')
        ROE = ROEDiv.text
        return ROE
    def get_operating_margin(self):
        OMDiv = driver.find_element_by_xpath('//*[@id="row4jqxgrid"]/div[3]/div')
        operatingmargin = OMDiv.text
        return  operatingmargin
    def get_pbratio(self):
        PBDiv = driver.find_element_by_xpath('//*[@id="row17jqxgrid"]/div[3]/div')
        pricebook = PBDiv.text
        return pricebook
    def get_debt(self,stonk):
        driver.get('https://www.macrotrends.net/stocks/charts/{}/qualcomm/balance-sheet'.format(stonk))
        DebtDiv = driver.find_element_by_xpath('//*[@id="row12jqxgrid"]/div[3]/div')
        debt = DebtDiv.text
        return debt
    def get_PE_ratio(self,stonk):
        driver.get('https://www.macrotrends.net/stocks/charts/{}/apple/pe-ratio'.format(stonk))
        PEDiv = driver.find_element_by_xpath('//*[@id="main_content"]/div[2]/span/strong')
        PE = PEDiv.text
        return PE
    def get_yield(self,stonk):
        driver.get('https://www.macrotrends.net/stocks/charts/{}/barclays/dividend-yield-history'.format(stonk))
        YieldDiv = driver.find_element_by_xpath('//*[@id="main_content"]/div[2]/span/strong[2]')
        Yield = YieldDiv.text
        return Yield
#   //*[@id="main_content"]/div[2]/span/strong[2]

##testing
# stonk = get_stonk_info("aapl")
# print(stonk.get_price())
# print(stonk.get_yield())
# print(stonk.get_PE_ratio())
# macro = get_financials_macrotrends("aapl")
# print(macro.get_ROE())
# print(macro.get_operating_margin())
# print(macro.get_pbratio())
# print(macro.get_debt("aapl"))
# print("Finished!!")
