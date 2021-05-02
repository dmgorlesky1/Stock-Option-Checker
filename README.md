# Author: Dillon Gorlesky
# Date: 04/24/2021

# Stock-Option-Checker
The purpose of this program is to see what stocks have options currently, and if options were added to a ticker.

# Notes:
The yahoo_fin package will occasionally error itself out and quit the program after too many attempts to get the a tickers information. This isn't unusual, just a nuiance of the package. You should be able to rerun it again and it will continue where it left off with no problems.

Future Work:
------------
-Check last trading day if the stock had options, if it didn't yesterday but does now, print to a text document the ticker name, and why it was added. 
    --> More information may be appended into the text file, will work on that when I get to it.
-Check if the options went from Monthly to Weekly
-Check for stocks that increase price cap
-If possible, I'd like to make some performance fixes, a way to automatically update the input file as new tickers IPOor go over my $120 range, and handle the program quitting before finishing (may just have it somehow rerun without any user interaction until finished)

