import os
from sys import argv
import sys
import DirectoryInfo as di
import RunRNN as rr
import pandas as pd
#***********************************************************#
#***********************************************************#
#*** MetaData.py is called from MProc.py to MultiProcess ***#
#***********************************************************#
#***********************************************************#

if __name__ == "__main__":

#Directory is the Directory that will either exist or be created
#to store the MetaData into a directory called Processed_Data
#Collects all the data from the Test_Stocks to run
    Directory = "Processed_Data"
    TestStock = "./Test_Stock/"
    try:
#StockList is the list of files in the Test_Stock Directory
#Stock is the Stock being processed.
#StockDir is the Stock csv file
#StockName is the Stock name of the csv file declared as StockDir
        StockList = os.listdir(TestStock)
        #Stock = int(argv[1])
        Stock = 1
        StockCSV = StockList[Stock]
        StockName = StockCSV[:-4]
        TestStockFile = TestStock + '/' + StockCSV
        Name = [(StockName)]
        StockCol = pd.DataFrame(Name, columns = ['Stock Name'])
        for i in range(1,30):
            StockCol = StockCol.append({'Stock Name' : StockName}, ignore_index=True)
    except:
        print("Data was not pulled correctly")
        sys.exit(0)

    try:
        #Epoch = int(argv[2])
        Epoch = 75
        #PredNumDays = int(argv[3])
        PredNumDays = 30
        PredOn= 60
        Years = 5
        StockDir = Directory + '/' + StockName
        di.CreateDir(StockDir)
        single = False
    except:
        print("Was unable to create the directory")
        sys.exit(0)
    try:
        for num in range(0, 6):
            Data = di.GetDataByDate(TestStockFile, Years, num*PredNumDays, single)
            Data = Data[num*PredNumDays:]
            Actual = Data[0:PredNumDays]
            Train = Data[PredNumDays:]
            Test = Train[0:PredNumDays]
            Actual = di.ResetDataStockData(Actual, True)
            Train = di.ResetDataStockData(Train, True)
            Test = di.ResetDataStockData(Test, True)
            try:
                PredStockPrice = rr.RunRNN(Train, Test, len(Train), len(Test), PredOn, Epoch)
            except:
                print("failed to RunRNN correctly")
                sys.exit(0)

            try:
                PredStock = pd.DataFrame(PredStockPrice[:, 0])
                PredStock.rename(columns = {0: 'predicted close'}, inplace=True)
                ActualStock = Actual.loc[:, ['timestamp', 'close']]
                ActualStock.rename(columns = {'close': 'actual close'}, inplace= True)
                PredStock = pd.concat([StockCol, ActualStock, PredStock], axis=1, join='inner')
                File = StockName + '_Epoch_' + str(Epoch) + '.csv'
                Title = ["Stock Name", "timestamp", "Actual Close", "Predicted Close"]
                # FIX ADD TO FILE TO ALLOW FOR MULTIPLE DAYS
                di.AddToFile(StockDir, File, Title, PredStock)
                print(str(num) + ' ' + File + ' Complete')
            except:
                print("failed to add to file")
                sys.exit(0)
    except:
        print("failed to split up the data")
        sys.exit(0)