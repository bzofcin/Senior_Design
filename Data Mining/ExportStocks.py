import urllib.request
import time
import os
import sys

stock_sym = ["AAPL", "GOOGL", "MSFT", "AMZN", "FB", "BRK-A" , "BRK-B" , "BABA", "JNJ", "JPM", "XOM", "BAC",
                "WMT", "WFC", "RDS-A", "RDS-B", "V", "PG", "BUD", "T", "CVX", "UNH", "PFE", "RHHBY", "CHL",
                "HD", "INTC", "VZ", "ORCL", "NVS"]

def downloadfiles(symbol):
#Downloads the files from Alphavantage and stores them in a file called Stock_Data

    Front ="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="
    Back = "&apikey=FI97CUETTHW9CX8Q&datatype=csv"
    urllib.request.urlretrieve(Front + symbol+ Back, "Stock_Data/" + symbol + ".csv")

def create():
#Checks to see if the Stock_Data File exists
#if it does it moves on, if it doesn't then creates the file location
	canCreate = "Stock_Data"

	print ("Verifying required files and directories...")
	if os.path.exists(canCreate) is False:
		print (canCreate + "/ Doesn't exist, creating it...")
		os.mkdir(canCreate)

	print ("Verification passed\n")


if __name__ == "__main__":
#calls function to create file location then stores files into Stock_Data
#Only 5 files can be downloaded per minute, so time.sleep(13) pauses the next files
#for 13 seconds. Currently 30 files are being downloaded per day which takes 6 minutes
#to complete
	create()

	for item in stock_sym:
		downloadfiles(item)
		time.sleep(13)

	sys.exit(0)