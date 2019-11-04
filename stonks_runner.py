#import statements
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import xlsxwriter
#import class get_stonk_info
from stonks import get_stonk_info,get_financials_macrotrends


# Set up excel file for parsing, some lists.

df = pd.read_excel('Equity_research.xlsx')
stonksList = df['Ticker']

# Creates the lists with empty values to prevent errors if it fails.
stonkprice = [""] * len(stonksList)
stonkPE = [""] * len(stonksList)
stonkPB = [""] * len(stonksList)
stonkoperatingmargin = [""] * len(stonksList)
stonkROE = [""] * len(stonksList)
stonkdebt = [""] * len(stonksList)
stonkyield = [""] * len(stonksList)
# FOM = [""] * len(stonksList)

# print(stonksList)
# for i in range(len(stonksList)):
#     x = i + 2
#     FOM[i] = "=((PERCENTRANK.INC(L$2:L35,L{})+1)*(PERCENTRANK.INC(J$2:J$35,J{})+1)*(PERCENTRANK.INC(I$2:I$35,I{})+1)/(PERCENTRANK.INC(G$2:G$35,G{})+1)/(PERCENTRANK.INC(F$2:F$35,F{})+1)/(PERCENTRANK.INC(K$2:K$35,K{})+1))".format(x,x,x,x,x,x)

print("-------------------getting NASDAQ info----------------------")
for i in range(len(stonksList)):
    stonk_price = get_stonk_info(stonksList[i])
    time.sleep(0.2)

    stonkpricetemp = stonk_price.get_price()
    stonkprice[i] = stonkpricetemp
    print(stonkpricetemp)



print("===================getting Macrotrends Info =======================")
for i in range(len(stonksList)):

    stonk_price = get_financials_macrotrends(stonksList[i])
    stonkpricetemp = stonk_price.get_ROE()
    stonkROE[i] = stonkpricetemp
    print(stonkpricetemp)

    stonkpricetemp = stonk_price.get_operating_margin()
    stonkoperatingmargin[i] = stonkpricetemp
    print(stonkpricetemp)

    stonkpricetemp = stonk_price.get_pbratio()
    stonkPB[i] = stonkpricetemp
    print(stonkpricetemp)
    # print("passing")
print("==============Getting Debt==================")
for i in range(len(stonksList)):
    stonk_info = get_financials_macrotrends(stonksList[i])
    stonkdebttemp = stonk_info.get_debt(stonksList[i])
    stonkdebt[i] = stonkdebttemp
    print(stonkdebttemp)
    # print("passing")
print("===========Getting PE Ratio=================")
for i in range(len(stonksList)):
    stonk_info = get_financials_macrotrends(stonksList[i])
    stonkPEtemp = stonk_info.get_PE_ratio(stonksList[i])
    stonkPE[i] = stonkPEtemp
    print(stonkPEtemp)
    # print("passing")
print("==========Getting Yield=================")
for i in range(len(stonksList)):
    stonk_price = get_financials_macrotrends(stonksList[i])
    stonkyieldtemp = stonk_price.get_yield(stonksList[i])
    stonkyield[i] = stonkpricetemp
    print(stonkyieldtemp)
    # print("passing")
df.drop(columns=['FOM'])
df ['Price'] = stonkprice
df ['PE '] = stonkPE
df ['PB'] = stonkPB
df ['Operating Margin'] = stonkoperatingmargin
df ['ROE'] = stonkROE
df ['Debt ($B)'] = stonkdebt
df ['Dividend Yield %)'] = stonkyield
# df['FOM'] = FOM
# df ['ticker'] = stonkticker
print(df)
with pd.ExcelWriter('stonksresearch.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1')

# print(stonksList)
# print(stonkprice)
# print(stonkticker)




# writer = pd.ExcelWriter('stonkresearch.xlsx', engine='xlsxwriter')
# stonks_instant.to_excel(writer, sheet_name='Sheet1')
# stonks_day.to_excel(writer, sheet_name='Sheet2')
# stonks_week.to_excel(writer, sheet_name='Sheet3')