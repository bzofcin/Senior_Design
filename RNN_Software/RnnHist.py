import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import os
import sys
from datetime import date, timedelta

# StockSym = {
# "ATVI":	"Activision Blizzard Inc",
# "ADBE":	"Adobe Inc.",
# "AMD":	"Advanced Micro Devices Inc",
# "ALGN":	"Align Technology Inc",
# "ALXN":	"Alexion Pharmaceuticals Inc",
# "AMZN":	"Amazon.com Inc",
# "AMGN":	"Amgen Inc",
# "AAL":	"American Airlines Group Inc",
# "ADI":	"Analog Devices Inc",
# "AAPL":	"Apple Inc",
# "AMAT":	"Applied Materials Inc",
# "ASML":	"ASML Holding NV",
# "ADSK":	"Autodesk Inc",
# "ADP":	"Automatic Data Processing Inc",
# "AVGO":	"Broadcom Inc",
# "BIDU":	"Baidu Inc",
# "BIIB":	"Biogen Inc",
# "BMRN":	"Biomarin Pharmaceutical Inc",
# "CDNS":	"Cadence Design Systems Inc",
# "CELG":	"Celgene Corp",
# "CERN":	"Cerner Corp",
# "CHKP":	"Check Point Software Technologies Ltd",
# "CHTR":	"Charter Communications Inc",
# "CTAS":	"Cintas Corp",
# "CSCO":	"Cisco Systems Inc",
# "CTXS":	"Citrix Systems Inc",
# "CMCSA":"Comcast Corp",
# "COST":	"Costco Wholesale Corp",
# "CSX":	"CSX Corp",
# "CTSH":	"Cognizant Technology Solutions Corp",
# "DLTR":	"Dollar Tree Inc",
# "EA":	"Electronic Arts",
# "EBAY":	"eBay Inc",
# "EXPE":	"Expedia Group Inc",
# "FAST":	"Fastenal Co",
# "FB":	"Facebook",
# "FISV":	"Fiserv Inc",
# "GILD":	"Gilead Sciences Inc",
# "GOOG":	"Alphabet Class C",
# "GOOGL":"Alphabet Class A",
# "HAS":	"Hasbro Inc",
# "HSIC":	"Henry Schein Inc",
# "ILMN":	"Illumina Inc",
# "INCY":	"Incyte Corp",
# "INTC":	"Intel Corp",
# "INTU":	"Intuit Inc",
# "ISRG":	"Intuitive Surgical Inc",
# "IDXX":	"IDEXX Laboratories Inc",
# "JBHT":	"J.B. Hunt Transport Services Inc",
# "JD":	"JD.com Inc",
# "KLAC":	"KLA Corp",
# "KHC":	"Kraft Heinz Co",
# "LRCX":	"Lam Research Corp",
# "LBTYK":"Liberty Global PLC",
# "LULU":	"Lululemon Athletica Inc",
# "MELI":	"Mercadolibre Inc",
# "MAR":	"Marriott International Inc",
# "MCHP":	"Microchip Technology Inc",
# "MDLZ":	"Mondelez International Inc",
# "MNST":	"Monster Beverage Corp",
# "MSFT":	"Microsoft Corp",
# "MU":	"Micron Technology Inc",
# "MXIM":	"Maxim Integrated Products Inc",
# "MYL":	"Mylan NV",
# "NTAP":	"NetApp Inc",
# "NFLX":	"Netflix Inc",
# "NTES":	"NetEase Inc",
# "NVDA":	"NVIDIA Corp",
# "NXPI":	"NXP Semiconductors NV",
# "ORLY":	"O'Reilly Automotive Inc",
# "PAYX":	"Paychex Inc",
# "BKNG":	"Booking Holdings Inc",
# "PYPL":	"PayPal Holdings Inc",
# "PEP":	"PepsiCo Inc.",
# "QCOM":	"Qualcomm Inc",
# "REGN":	"Regeneron Pharmaceuticals Inc",
# "ROST":	"Ross Stores Inc",
# "SIRI":	"Sirius XM Holdings Inc",
# "SWKS":	"Skyworks Solutions Inc",
# "SBUX":	"Starbucks Corp",
# "SNPS":	"Synopsys Inc",
# "TTWO":	"Take-Two Interactive Software Inc",
# "TSLA":	"Tesla Inc",
# "TXN":	"Texas Instruments Inc",
# "TMUS":	"T-Mobile US Inc",
# "ULTA":	"Ulta Beauty Inc",
# "UAL":	"United Airlines Holdings Inc",
# "VRSN":	"Verisign Inc",
# "VRSK":	"Verisk Analytics Inc",
# "VRTX":	"Vertex Pharmaceuticals Inc",
# "WBA":	"Walgreens Boots Alliance Inc",
# "WDC":	"Western Digital Corp",
# "WDAY":	"Workday Inc",
# "WYNN":	"Wynn Resorts Ltd",
# "XEL":	"Xcel Energy Inc",
# "XLNX":	"Xilinx Inc"
# }

StockSym = {
"GOOGL":"Alphabet Class A"
}

def GetData(stock):
    front = "./Stock_Data/"
    end = ".csv"
    filePath = front + stock + end
    today = date.today();
    lastYear = today -  timedelta(days=1825)
    formatedYear = lastYear.strftime("%Y-%m-%d")
    try:
        fullData = pd.read_csv(filePath)
        fullData.sort_values(by="timestamp",inplace=True,ascending=False)
        trainTestData = fullData.loc[fullData["timestamp"] >= formatedYear]
        return trainTestData
    except:
        print("File " + stock + " was not found and could not be opened.")



if __name__ == "__main__":
    yesterday = date.today() - timedelta(days=7);
    formatedYesterday = yesterday.strftime("%Y-%m-%d")
    for item in StockSym:
        TrainData = GetData(StockSym.get(item))
        try:
            TestData = TrainData.loc[TrainData["timestamp"] >= formatedYesterday]
            TrainData = TrainData.loc[TrainData["timestamp"] <= formatedYesterday]
            TestData.sort_values(by="timestamp",inplace=True,ascending=True)
            TrainData.sort_values(by="timestamp",inplace=True,ascending=True)
        except:
            print("Failed to split up the testing and training data")

        try:
            training_set = TrainData.iloc[:, 4:5].values
            sc = MinMaxScaler(feature_range=(0, 1))
            training_set_scaled = sc.fit_transform(training_set)
            X_train = []
            y_train = []
            for i in range(60, len(TrainData)):
                X_train.append(training_set_scaled[i - 60:i, 0])
                y_train.append(training_set_scaled[i, 0])
            X_train, y_train = np.array(X_train), np.array(y_train)
            X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
            os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
            regressor = Sequential()
            regressor.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    # 20% of ther neurons will be dropped out. this  means that 10 cells wil be ignored out of 50
            regressor.add(Dropout(0.2))
    # dont need to speciy input shape it is alredy specified
    # Adding a second LSTM layer and some Dropout regularisation
            regressor.add(LSTM(units=50, return_sequences=True))
            regressor.add(Dropout(0.2))

    # Adding a third LSTM layer and some Dropout regularisation
            regressor.add(LSTM(units=50, return_sequences=True))
            regressor.add(Dropout(0.2))

    # Adding a fourth LSTM layer and some Dropout regularisation
            regressor.add(LSTM(units=50))
            regressor.add(Dropout(0.2))

    # Adding the output layer
    # fully connected layer using dnese class
    # same at ann
    # number of neurons needed to be in the output layer.
    # the unit correstponds to the number of neurons that need to be in the oupout layer
    # this is based off the dimension of the ouput which is 1
            regressor.add(Dense(units=1))

    # Compiling the RNN
    # adam optimizer look up what it means
    # using mean squared for loss function
            regressor.compile(optimizer='adam', loss='mean_squared_error')

    # Fitting the RNN to the Training set
    # this fits the information to the training set
    # first input is the training set and ouptut of prediction which is compared to ytrain
    # the next inout is the y train which is the comparison of the
    # batch size is the size of batch going into
            regressor.fit(X_train, y_train, epochs=50, batch_size=100)
        except:
            print("Failed at epochs")
        try:
            real_stock_price = TestData.iloc[:, 4:5].values
            dataset_total = pd.concat((TrainData['close'], TestData['close']), axis=0)
            inputs = dataset_total[len(dataset_total) - len(TestData) -60:].values
            inputs = inputs.reshape(-1, 1)
            inputs = sc.transform(inputs)
            X_test = []
        # info foroutput the 60 days past to predict the next 20 days.
            for i in range(60, 66):
                X_test.append(inputs[i - 60:i, 0])
            X_test = np.array(X_test)
            X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
            predicted_stock_price = regressor.predict(X_test)
        # get original scale of predicted values
            predicted_stock_price = sc.inverse_transform(predicted_stock_price)

            predicted_length = len(predicted_stock_price)-1
            # trend up == 1; trend down == 0; no change == 2
            predicted_trend = 0
            real_trend = 0
            total = 0
            accurate = 0
            percent_accurate = 0
            for i in range(1, predicted_length):
                if predicted_stock_price[i] > predicted_stock_price[i - 1]:
                    predicted_trend = 1
                elif predicted_stock_price[i] < predicted_stock_price[i - 1]:
                    predicted_trend = 0
                elif predicted_stock_price[i] == predicted_stock_price[i - 1]:
                    predicted_trend = 2

                if real_stock_price[i] > real_stock_price[i - 1]:
                    real_trend = 1
                elif real_stock_price[i] < real_stock_price[i - 1]:
                    real_trend = 0
                elif real_stock_price[i] == real_stock_price[i - 1]:
                    real_trend = 2

                if predicted_trend == real_trend:
                    accurate += 1

                total += 1

            percent_accurate = (accurate / total) * 100
            print("Accuracy: " + str(percent_accurate) + "%")

        # Calculating accuracy
            plt.plot(real_stock_price, color='red', label='Real ' + StockSym.get(item) + ' Stock Price')
            plt.plot(predicted_stock_price, color='blue', label='Predicted ' + StockSym.get(item) + ' Price')
            plt.title(StockSym.get(item) +' Stock Price Prediction')
            plt.xlabel('Time in Days')
            plt.ylabel(StockSym.get(item) +' Stock Price')
            plt.legend()
            plt.show()
        except:
            print("failed after epochs")

    sys.exit(0)











