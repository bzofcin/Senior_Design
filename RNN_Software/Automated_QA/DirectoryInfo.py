import os
import csv
from datetime import date, timedelta
import pandas as pd

def AddToFile(StockFile, file, title, df):
    df.columns = range(df.shape[1])
    print("Determining if " + file + " exists")
    if os.path.isfile(StockFile + "/" + file):
        print(StockFile + "/" + file + "/ exists")
        print("Adding row to " + file)
        with open(StockFile + "/" + file, "a") as fp:
            wr = csv.writer(fp, dialect='excel')
            for index, row in df.iterrows():
                wr.writerow(row)
        fp.close()
    else:
        print(file + " does not exist.  Creating file...")
        print("Adding title to " + file)
        print("Adding row to " + file)
        with open(StockFile + "/" + file, "a") as fp:
            wr = csv.writer(fp, dialect = 'excel')
            wr.writerow(title)
            for index, row in df.iterrows():
                wr.writerow(row)
        fp.close()

def CreateDir(StockDir):

    print("Determining if " + StockDir + " directory exists...")
    if os.path.exists(StockDir) is False:
        print(StockDir + "/ Does not exist, creating it...")
        os.mkdir(StockDir)
        print(StockDir + "/ is created")
    else:
        print("Directory Exists")

    print("Directory Creation is complete")

def GetDataByDate(StockFile, years, day, single):

    HistData = (date.today() - timedelta(days=(int(years*365)))).strftime("%Y-%m-%d")
#EndData = (date.today() - timedelta(days=(int(day)))).strftime("%Y-%m-%d")
    try:
        fullData = pd.read_csv(StockFile)
        fullData.sort_values(by="timestamp",inplace=True,ascending=False)
        dataLen = len(fullData.loc[fullData["timestamp"] > HistData])
        if single is True:
            trainTestData = fullData.iloc[day : dataLen+day]
        else:
            trainTestData = fullData.iloc[0: dataLen+day]
        return trainTestData
    except:
        print("File " + StockFile + " was not found and could not be opened.")

def ResetDataStockData(df):
    df.sort_values(by="timestamp", inplace=True, ascending=True)
    df = df.set_index('timestamp')
    df = df.reset_index()
    return df