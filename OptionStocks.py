from yahoo_fin.options import *
from yahoo_fin import options
from yahoo_fin.stock_info import *
import requests
from pandas import *
import os
import sys
import csv
import math
from difflib import Differ
from datetime import date
import shutil

#STEPS
#1. Read in file used to keep track of previous logs
#2. Read in FinalTickers.csv
#3. Compare each line in the two files. PreviousLogs will have a field either 'Y' or 'N' if it had options last
#       time the program was ran.
#4a. Write to a temp file an updated options log
#4b. Print to screen if a ticker is found to have recently had options added.
#5. Merge the temp file into the previous logs file
#6. Delete temp file


#The file holding the previous logs of if a ticker had options or not last time the program was ran.
prevLog = open("previousLog.csv", "r+")

#This will allow for me to compare as the tickers are being checked for options
content = prevLog.readlines()

#The file all the filtered stocks get written to from NYSE and NASDAQ listings
finalFile = open("finalTickers.csv", "r")

#Temp file that holds the updated values on if the stocks have options 
tempFile = open("tempFile.csv", "w")

#File to hold the tickers that recently have options added to them
hasOptions = open("newOptions.txt", "w")

#This is how I initiated the prevLog file
#for aline in finalFile:
    #values = aline.split(",")
    #val = values[0] + ",N\n"
    #prevLog.write(val)

#Formatted string for new run that goes into newOptions.txt file
today = date.today()
hasOptions.write("<--------------------> " + str(today) + " <-------------------->\n")


i = 0
for aline in finalFile:
    values = aline.split(",")
    try:
        get_calls(values[0])
        line = values[0] + ": added options recently.\n"
        print(values[0] + " Yes")
        cont = content[i]
        conts = cont.split(",")
        if conts[1] == "N\n":
            print(line)
            hasOptions.write(line)
            hasOptions.flush()
            
            
        tempFile.write(cont)
        tempFile.flush()
    except:
        print(values[0] + " No")
        tempFile.write(aline)
        tempFile.flush()
        continue
    
    i = i + 1


tempFile.flush()
hasOptions.flush()

shutil.move(tempFile, previousLog)

tempFile.close()
hasOptions.close()
prevLog.close()
finalFile.close()


