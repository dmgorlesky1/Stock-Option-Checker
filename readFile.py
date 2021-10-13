import csv
import re
from yahoo_fin.options import *
from yahoo_fin import options
from yahoo_fin.stock_info import *
import requests
from pandas import *
import os
import sys
import csv
import math

#The file all the filtered stocks get written to from NYSE and NASDAQ listings
finalFile = open("finalTickers.csv", "w")

#Regex's I use to filter stocks out of the list
regexPer = re.compile(r'%')
regexSenior = re.compile(r'[Ss]enior')
regexWar = re.compile(r'[Ww]arrant')
regexDiv = re.compile(r'[Dd]ividend')
regexInFu = re.compile(r'[Ii]ncome [Ff]und')
regexLong = re.compile(r'[Cc]ommon [Ss]hares of [Bb]eneficial [Ii]nterest')
regexDivTru = re.compile(r'[Dd]ividend [Tt]rust')
regexEach = re.compile(r'[Ee]ach [Rr]epresenting')
regexUnit = re.compile(r'[Uu][Nn][Ii][Tt]')
regexDivFun = re.compile(r'[Dd]ividend [Ff]und')
regexInTru = re.compile(r'[Ii]ncome [Tt]rust')
regexDepo = re.compile(r'[Dd]epositary [Ss]hare')
regexFixed = re.compile(r'[Ff]ixed-[Ii]ncome')

#STEPS
#1. Read in NYSE file
#2.a Skip subs (ACAC, ACACC, ACACW)
#2.b Skip Senior Notes (Names have a %, "Dividend", "Senior", "Warrant"
#3. Skip tickers over $100
#4. Add to file
#5. Repeat 1-4 but with Naqdaq file
#6. Remove dual-listed companies from final file

file = open("NYSEFile.csv", "r")
maths = True
#This is used to make it continue to run if it encounters an exception because the
#Yahoo_fin package will occassionally not make a proper connection and quit.
#This is to prevent from having to start all over
while maths:
    try:
        for aline in file:
            values = aline.split(",")
            print(values[0])
            if not regexPer.search(values[1]):
                if not regexSenior.search(values[1]):
                    if not regexWar.search(values[1]):
                        if not regexDiv.search(values[1]):
                            if not regexInFu.search(values[1]):
                                if not regexLong.search(values[1]):
                                    if not regexDivTru.search(values[1]):
                                        if not regexEach.search(values[1]):
                                            if not regexUnit.search(values[1]):
                                                if not regexDivFun.search(values[1]):
                                                    if not regexInTru.search(values[1]):
                                                        if not regexDepo.search(values[1]):
                                                            if not regexFixed.search(values[1]):
                                                                if "Symbol" not in aline:
                                                                    ticker = str(values[2])
                                                                    ticker = ticker[1:]
                                                                    if float(ticker) <= 100.00:
                                                                        finalFile.write(aline)
                                        
        maths = False
    except:
        continue
    

file.close()


print("-----------------------------------------")
file2 = open("NASDAQFile.csv", "r")
maths = True
while maths:
    try:
        for aline in file2:
            values = aline.split(",")
            print(values[0])
            if not regexPer.search(values[1]):
                if not regexSenior.search(values[1]):
                    if not regexWar.search(values[1]):
                        if not regexDiv.search(values[1]):
                            if not regexInFu.search(values[1]):
                                if not regexLong.search(values[1]):
                                    if not regexDivTru.search(values[1]):
                                        if not regexEach.search(values[1]):
                                            if not regexUnit.search(values[1]):
                                                if not regexDivFun.search(values[1]):
                                                    if not regexInTru.search(values[1]):
                                                        if not regexDepo.search(values[1]):
                                                            if not regexFixed.search(values[1]):
                                                                if "Symbol" not in aline:
                                                                    ticker = str(values[2])
                                                                    ticker = ticker[1:]
                                                                    if float(ticker) <= 100.00:
                                                                        finalFile.write(aline)
                                        
        maths = False
    except:
        continue
    

file2.close()                                                
finalFile.close()