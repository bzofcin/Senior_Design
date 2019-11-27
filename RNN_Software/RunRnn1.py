
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import os

def RunRNN1(theStock, predictOn, epoch):
    BADTESTS = "../Data Mining/TestDir/"
    mylist = os.listdir(BADTESTS)
    num1 =  theStock
    print("Running " + mylist[num1] + "from " + str(num1))
    test = mylist[num1]
    dataset_train = pd.read_csv(BADTESTS + test)
    test = "NASDAQ Composite.csv"
    aditional_data = pd.read_csv(BADTESTS + test)
    aditional_data.sort_values(by="timestamp", inplace=True, ascending=False)
    dataset_train['NasOpen'] = aditional_data['open']
    dataset_train['NasClose'] = aditional_data['close']
    dataset_train['NasHigh'] = aditional_data['high']
    dataset_train['Naslow'] = aditional_data['low']
    n_future = 7  # Number of days you want to predict into the future
    n_past = predictOn  # Number of past days you want to use to predict the future
    dataset_train.drop(dataset_train.tail(n_future).index, inplace=True)
    dataset_train.sort_values(by="timestamp", inplace=True, ascending=True)
    cols = list(dataset_train)[1:11]
    dataset_train = dataset_train[cols].astype(str)
    for i in cols:
        for j in range(0, len(dataset_train)):
            dataset_train[i][j] = dataset_train[i][j].replace(",", "")

    dataset_train = dataset_train.astype(float)
    training_set = dataset_train.as_matrix()
    sc = StandardScaler()
    training_set_scaled = sc.fit_transform(training_set)
    sc_predict = StandardScaler()
    sc_predict.fit_transform(training_set[:, 0:1])
    X_train = []
    y_train = []
    for i in range(n_past, len(training_set_scaled) - n_future + 1):
        X_train.append(training_set_scaled[i - n_past:i, 0: 10])
        y_train.append(training_set_scaled[i + n_future - 1:i + n_future, 1])

    X_train, y_train = np.array(X_train), np.array(y_train)
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    regressor = Sequential()
    regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (n_past , 9)))
    regressor.add(Dropout(0.2))
    regressor.add(LSTM(units=50, return_sequences=True))
    regressor.add(Dropout(0.2))
    regressor.add(LSTM(units=50, return_sequences=True))
    regressor.add(Dropout(0.2))
    regressor.add(LSTM(units=50, return_sequences=True))
    regressor.add(Dropout(0.2))
    regressor.add(LSTM(units=50))
    regressor.add(Dropout(0.2))
    regressor.add(Dense(units=1))
    regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
    regressor.fit(X_train, y_train, epochs=epoch, verbose=2, use_multiprocessing=True)
    predictions = regressor.predict(X_train[-n_future:])
    predicted_stock_price = sc_predict.inverse_transform(predictions)
    return predicted_stock_price