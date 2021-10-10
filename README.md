# Author: Dillon Gorlesky
# Date: 04/24/2021

# Stock-Option-Checker
The purpose of this program is to see what stocks have options currently, and if options were added to a ticker.

# Notes:
The yahoo_fin package will occasionally error itself out and quit the program after too many attempts to get the a tickers information. This isn't unusual, just a nuiance of the package. The readFile program will continue to run through all the tickers, filtering out all the undesired, as well as tickers above $100.

Future Work:
------------
-Check last trading day if the stock had options, if it didn't yesterday but does now, print to a text document the ticker name, and why it was added. 
    
    --> More information may be appended into the text file, will work on that when I get to it.

-Check if the options went from Monthly to Weekly

-Check for stocks that increase price cap

-If possible, I'd like to make some performance fixes, a way to automatically update the input file as new tickers IPO, or go over my $100 range. I'd also like for it to handle the program quitting before finishing (may just have it somehow rerun without any user interaction until finished)

# Data:
All of my data for tickers on the NYSE and NASDAQ come from 
```https://www.nasdaq.com/market-activity/stocks/screener?exchange=NYSE&render=download```

The NYSEFile.csv holds all the tickers on the NYSE exchange.
The NASDAQ.csv holds all the tickers on the NASDAQ exchange.
The finalTickers.csv holds all the filtered tickers 
The previousLog.csv file will hold the data of each ticker from the last time the program was ran.
The tempFile.csv will hold the updated values that will then overwrite previousLog (don't want data lost or overwritten as I'm reading)
The newOptions.txt file holds the tickers that now have options that didn't previously. Data will eventually be appended at the top instead of being overwritten.
