from yahoo_fin.stock_info import *
from pandas import *
import os
import sys
import csv
import math

#print(tickers_dow())

#This will read in the csv file --> Works as relative path bc it's in same directory
df = pd.read_excel (r'StockTickerTester.xlsx')

#This gets the Symbols column from the df Dataframe
stockTicker=df["Symbol"]

print(stockTicker)

