import os
import pandas as pd
import accuracy_stats as acs
import DirectoryInfo as di

Directory = "Processed_Data"
StockDir = os.listdir(Directory)


for i in range(0,len(StockDir)):
    Stocks = os.listdir(Directory + '/' + StockDir[i])
    for j in range(0, len(Stocks)):
        FilePath = Directory +'/' + StockDir[i] +'/' + Stocks[j]
        StockFile = pd.read_csv(FilePath)
        StockFile = di.ResetDataStockData(StockFile, True)
        ActData = StockFile['Actual Close']
        PredData = StockFile['Predicted Close']
        Accuracy = acs.calculate_accuracy(PredData, ActData)
        print(Stocks[j], Accuracy)

