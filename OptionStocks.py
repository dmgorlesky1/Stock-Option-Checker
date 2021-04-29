from yahoo_fin.options import *
from yahoo_fin import options
from yahoo_fin.stock_info import *
from pandas import *
import os
import sys
import csv
import math

#This is the file I will keep track of the last index of
#CSV file ran so I don't have to restart if an error occurs.
file1 = open("myFile.txt", "r")

pos = file1.readline()
try:
    #If it didn't get to the first 20 spots
    if(int(pos) < 20):
        pos = "0"
except:
    pos = "0"
    

file2 = open("myFile.txt", "w")
file2.write(str(pos))
file2.close()

#This will read in the csv file --> Works as relative path bc it's in same directory
#df = pd.read_excel (r'StockTickerTester.xlsx')
#df = pd.read_excel (r'StocksWithOptions.xlsx')
df = pd.read_excel (r'StockTickers.xlsx')
#df = pd.read_excel (r'AssortedStocks.xlsx')

#print(df)

#This gets the Symbols column from the df Dataframe
stockTicker=df["Symbol"]

#This splices the Dataframe to be ones we haven't checked yet
stockTicker=stockTicker.iloc[int(pos):]

i=1
k=int(pos)
#This is removing stocks with a price greater than 120
#Also, this is assuming every stock over $120 has options and will be weekly
try:
    for ticker in stockTicker:
        ticker = str(ticker)
        ticker = ticker.strip()
        price = get_live_price(ticker)
        price = '%.2f' % price
        print(k)
        if float(price) > 120:
            print(ticker + " Delete------------------------------------")
            print(" Delete------------------------------------")
            print(" Delete------------------------------------")
            print(" Delete------------------------------------")
    

        k = k + 1
        if(i == 20):
            file2 = open("myFile.txt", "w")
            file2.truncate()
            file2.write(str(k))
            file2.close()
            file2 = open("myFile.txt", "r")
            i = 0
            
        i = i + 1

except Exception as e: #Catch every exception so I can put the number I'm at currently into a text file
    file2 = open("myFile.txt", "w")
    file2.truncate()
    file2.write(str(k))
    file2.close()
    print(e)
    exit()

#Got to end of file, now to set next time back to 0
file2 = open("myFile.txt", "w")
file2.truncate()
file2.write("0")
file2.close()
#Checking if the stock has options
has_options={}
no_options={}
i=0
# for ticker in stockTicker:
    #try:
     #   has_options[ticker] = get_calls(ticker)
    #except Exception:
        #Need to add stuff here to update the file so if used tomorrow it knows yesterday it didn't
        #print(ticker + " failed")
        #no_options[i] = ticker
     #   i = 1

#print(stockTicker)
#print(no_options)
print("---------------------------------------")
#print(has_options)

