#import statements
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import xlsxwriter
from GetInfoOne import GetOneInfoUSA
#import class get_stonk_info
from stonks import get_stonk_info,get_financials_macrotrends


# Set up excel file for parsing, some lists.

<<<<<<< HEAD
<<<<<<< HEAD
df = pd.read_excel('stonksresearch.xlsx')
print(df)
=======
df = pd.read_excel('Equity_research.xlsx')
>>>>>>> parent of aceba20... finally
=======
df = pd.read_excel('Equity_research.xlsx')
>>>>>>> parent of aceba20... finally
analysis = []
stonksList = df['Ticker'].to_list()

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
kowalski = GetOneInfoUSA()
print("-------------------getting NASDAQ info----------------------")
for i in range(len(stonksList)):
    try:
        analysis.append(kowalski.get_info(stonksList[i]))
    except:
        print('fail')
        # stonksList.remove(stonksList[i])
# df.drop(columns=['FOM'])
# df ['Price'] = stonkprice
# df ['PE '] = stonkPE
# df ['PB'] = stonkPB
# df ['Operating Margin'] = stonkoperatingmargin
# df ['ROE'] = stonkROE
# df ['Debt ($B)'] = stonkdebt
# df ['Dividend Yield %)'] = stonkyield
# # df['FOM'] = FOM
# # df ['ticker'] = stonkticker
# print(df)
print(analysis)
df = pd.DataFrame(analysis, columns=['Ticker','Price', 'PE','PB','Operating Margin','ROE','Debt','Yield','50 Day Average','200 Day Average', 'Golden Cross'])
FOMScore = ((df['Debt'].rank(na_option='bottom',pct=True)) * (df['PB'].rank(na_option='bottom',pct=True)) * (df['PE'].rank(na_option='bottom',pct=True)))
df = df.insert(11,"Figure Of Merit Score",FOMScore)
# FOMRank = (df['Figure Of Merit Rank'].rank(na_option='bottom',pct=True))
# df = df.insert(11,"Figure Of Merit Rank",FOMRank)

print(df)
# with pd.ExcelWriter('stonksresearch.xlsx') as writer:
#     df.to_excel(writer, sheet_name='Sheet1')
#
