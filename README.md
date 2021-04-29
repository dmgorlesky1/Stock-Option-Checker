# Author: Dillon Gorlesky
# Date: 04/24/2021

# Stock-Option-Checker
The purpose of this program is to see what stocks have options currently.

# Notes:
The yahoo_fin package will occasionally error itself out and quit the program after too many attempts to get the a tickers information. This isn't unusual, just a nuiance of the package. You should be able to rerun it again and it will continue where it left off with no problems.

Future Work:
------------
-Check last trading day if the stock had options, if not print to a text document the ticker name and a description of why it was added.
-Check if the options went from Monthly to Weekly or vis versa
-Check for stocks that increase price cap

