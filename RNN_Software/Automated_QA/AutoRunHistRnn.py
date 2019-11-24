import os
import time

if __name__ == '__main__':

#Stock_Dir should point to where the Stock_Data is in the directory
#If running of the repository, location is "../Data Mining/Stock_Data"
#The filenames will be stored into the list Stocks
    Stock_Dir = r"C:\Users\Terran\Documents\seniorprojectfall2019team7\RNN_Software\Automated_QA\TestDir"
    Stocks = os.listdir(Stock_Dir)
    StockNum = 0

    #Runs RnnHist.py for 30 days on each Stock in Stock_Dir
    #Passes the stock to run and the day to predict
    for item in Stocks:
        for counter in range(30, 29, -1):
            os.system('python ./RnnHist.py ' + str(StockNum) + ' ' + str(counter))
        StockNum = StockNum + 1
        print("Stock " + item + " is Processed")
    print("All Stocks Processed")