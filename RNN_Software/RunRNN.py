
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import os

def RunRNN(TrainData, TestData, TrainLen, TestLen, predictOn, epoch):
    training_set = TrainData.iloc[:, 4:5].values
    sc = MinMaxScaler(feature_range=(0, 1))
    training_set_scaled = sc.fit_transform(training_set)
    X_train = []
    y_train = []
    for i in range(predictOn, TrainLen):
        X_train.append(training_set_scaled[i - predictOn:i, 0])
        y_train.append(training_set_scaled[i, 0])
    X_train, y_train = np.array(X_train), np.array(y_train)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    regressor = Sequential()
    regressor.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    regressor.add(Dropout(0.2))
    regressor.add(LSTM(units=50, return_sequences=True))
    regressor.add(Dropout(0.2))
    regressor.add(LSTM(units=50, return_sequences=True))
    regressor.add(Dropout(0.2))
    regressor.add(LSTM(units=50))
    regressor.add(Dropout(0.2))
    regressor.add(Dense(units=1))
    regressor.compile(optimizer='adam', loss='mean_squared_error')
    regressor.fit(X_train, y_train, epochs=epoch, verbose=2, use_multiprocessing=True)

    dataset_total = pd.concat((TrainData['close'], TestData['close']), axis=0)
    inputs = dataset_total[len(dataset_total) - len(TestData['close']) - predictOn:].values
    inputs = inputs.reshape(-1, 1)
    inputs = sc.transform(inputs)
    X_test = []
    for i in range(predictOn, predictOn + TestLen):
        X_test.append(inputs[i - predictOn:i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    predicted_stock_price = regressor.predict(X_test)
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)
    return predicted_stock_price