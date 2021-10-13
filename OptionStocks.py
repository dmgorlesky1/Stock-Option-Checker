from yahoo_fin.options import *
from yahoo_fin.stock_info import *
import requests
from pandas import *
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

#The file all the filtered stocks get written to from NYSE and NASDAQ listings
finalFile = open("finalTickers.csv", "r")

#Temp file that holds the updated values on if the stocks have options 
tempFile = open("tempFile.csv", "w")
tempFile.truncate() #Making sure the temp files are empty before more info is added

#File to hold the tickers that recently have options added to them
hasOptions = open("newOptions.txt", "r+")

#Logs temporary output in order to keep track of previous logs
tempOption = open("tempLogs.txt", "a+")
tempOption.truncate() #Making sure the temp files are empty before more info is added


#This is how I initiated the prevLog file
# for aline in finalFile:
#     values = aline.split(",")
#     val = values[0] + ",N\n"
#     prevLog.write(val)


#Formatted string for new run that goes into newOptions.txt file
today = date.today()
tempOption.write("<--------------------> Tickers with New Options <-------------------->\n")
tempOption.write("                             " + str(today) + "                       \n")

k = 1
i = 0

for aline in prevLog:
      values = aline.split(",")
      print("Ticker " + str(k) + ": " + values[0]) #This is to print what ticker and # program is on.
      k = k + 1
      try:
        get_calls(values[0])
        #print("After get calls") #THIS IS USED WHEN YOU WANT TO MAKE SURE IT ISN'T STUCK
        line = values[0] + ": added options recently.\n"
        if values[1] == "N\n":
            tempOption.write(line)
            tempOption.flush()
            temp = values[0] + ",Y\n" #Updating file so next time it sees it does have options
            tempFile.write(temp)
            tempFile.flush()
        else:      
            tempFile.write(aline)
            tempFile.flush()
      except:
        #print("except") #THIS IS USED WHEN YOU WANT TO MAKE SURE IT ISN'T STUCK
        tempFile.write(aline)
        tempFile.flush()
        continue
      
 
tempFile.flush()
tempOption.flush()


#Adding spacing on temp file
tempOption.write("\n\n")


#Appending old logs onto temp file
tempOption.write(hasOptions.read())
tempOption.close()
hasOptions.close()


#Reopening in order to read and write, then move temp file to newOptions
hasOptions = open("newOptions.txt", "r+")
tempOption = open("tempLogs.txt", "r+")
shutil.copyfile("tempLogs.txt", "newOptions.txt")
tempOption.truncate() #Clearing temp file


#Closing files
tempOption.close()
hasOptions.close()
prevLog.close()
tempFile.close()


#Moving new list of stocks with options back to previousLog file
prevLog = open("previousLog.csv", "r+")
tempFile = open("tempFile.csv", "r+")
shutil.copyfile("tempFile.csv", "previousLog.csv") #<--------------------------------------------
tempFile.truncate() #Clearing temp file


#Final closing statements
tempFile.close()
prevLog.close()
finalFile.close()


