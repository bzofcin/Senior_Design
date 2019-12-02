import numpy as np
import pandas as pd
import os
import sys
from datetime import date, timedelta
import time
import DirectoryInfo as di
import RunRNN as rr
from sys import argv
#************************************************************************
#****************This code is not to be run by itself********************
#************************************************************************
#*************Run this code by running AutoRnnHistRnn.py*****************
#************************************************************************


#Stock_Dir should point to where the Stock_Data is in the directory
#If running of the repository, location is "../Data Mining/Stock_Data"
#The filenames will be stored into the list Stocks
#Directory is where the Predicted Data will be placed
#if you run it as is, the Predicted folder will be created inside RNN_Software
#Consider where you would like to store that data before running
Stock_Dir = "../Data Mining/TestDir/"
Stocks = os.listdir(Stock_Dir)
Directory = "Prediction_Test"

if __name__ == "__main__":
    #num takes in a passed argument from AutoRunHistRnn.py which lets RnnHist.py
    #which stock to run from Stocks
    #predInterval takes in a passed argument from AutoRunnHistRnn.py which lets
    #RnnHist.py know how many stock days to run
    num = int(argv[1])
    predInterval = int(argv[2])


    #For now Datepredict should always be 1.  This will run the RNN once for each day
    #until predInterval is met
    datepredict = 30


    # ************************************************************************
    # **************************Adjustable Data*******************************
    # ************************************************************************
    #PredictOn is the number of days the RNN trains to predict a day
    #epoch is then number of epochs to run
    #years in the amount of historical data it will be trained on
    predictOn = 120
    epoch = 50
    years = 10
    single = False



    #This code is designed to provide a systematic way categorizing the data
    #In the Predicted Folder, A Directory will be created based on the Adjusted Data Above
    #Example: E_50_P0_60_DP_1_H_5 translates:
    #epoch = 50, predictOn = 60, datepredict = 1, years = 5
    #All files ran with that configuration will be stored in that directory
    DirName = "E_" + str(epoch) + "_PO_" + str(predictOn) + "_DP_" + str(datepredict) + "_H_" + str(years)
    Title = ["timestamp", "close"]
    StockName = Stocks[num]
    #StockName = StockName[:-4]
    print(StockName)
    File = DirName + "_" + StockName
    dir = Stock_Dir + "/" + Stocks[num]


    #This code calls GetDataByDate from a created library called DirectoryInfo
    Data = di.GetDataByDate(dir, years, predInterval, single)

    try:
        #ActualData is stored separately.  In the regular RNN, this would be the data
        #that we are trying to predict as those dates have not happened yet.  For
        #this program the ActualData is used to make the comparison on what is predicted
        #ActualData is currently set to only have one day's value
        #Testing Data have 2 days
        #Training Data will have the remaining historical data and encompass the Testing Data
        ActualData = Data.iloc[0:datepredict]
        TestData = Data.iloc[datepredict:2*datepredict]
        TrainData = Data.iloc[datepredict:len(Data)+1]
        TestData = di.ResetDataStockData(TestData)
        TrainData = di.ResetDataStockData(TrainData)
        ActualData = di.ResetDataStockData(ActualData)
        TrainLen = len(TrainData)
        TestLen = len(TestData)
        ActualLen = len(ActualData)
    except:
        print("Failed to split up the testing and training data")

        #This is where the RNN runs.  Rnn has been moved to a library called RunRNN with
        #the method called RunRNN.  the predicted stocks will return from the method
        #StartTime and EndTime are used to calculate the actual time to run the RNN.
    StartTime = time.time()
    try:
        predicted_stock_price = rr.RunRNN(TrainData, TestData, TrainLen, TestLen, predictOn, epoch)
    except:
        print("failed during rnn process")
    EndTime = time.time()


    try:
        #real_stock_price stores the close value of ActualData (The data we want to predict)
        #df_Pred_Stock joins the Predicted Stock price with the corresponding date that is being
        #predicted
        real_stock_price = ActualData.iloc[:, 4:5].values
        df_Pred_Stock = pd.DataFrame(predicted_stock_price[:,0])
        Date_data = ActualData.iloc[:, 0:1]
        Date_data = Date_data.set_index('timestamp')
        Date_data = Date_data.reset_index()
        df_Pred_Stock = pd.concat([Date_data, df_Pred_Stock], axis=1, join='inner')


        #CreateDir is called to create the Predicted Directory, if it already exists, nothing happens
        #The file path for the predicted data files is created, and the directory is created by the
        #CreateDir method.
        di.CreateDir(Directory)
        FileDir = Directory + "/" + DirName
        di.CreateDir(FileDir)
        #FIX ADD TO FILE TO ALLOW FOR MULTIPLE DAYS
        di.AddToFile(FileDir, File, Title, df_Pred_Stock)

        #Stats printed
        print(Stocks[num])
        print("--- " + str(EndTime - StartTime) + " seconds ---")
    except:
        print("failed after epochs")

    sys.exit(0)












