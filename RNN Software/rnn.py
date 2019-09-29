# Recurrent Neural Network

# Part 1 - Data Preprocessing

# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the training set
dataset_train = pd.read_csv('Google_Stock_Price_Train.csv')
# Create training set array
# [:, 1:2] imports column 1 (indexing from zero) from data sheet
training_set = dataset_train.iloc[:, 1:2].values

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
# Normalisation: x_norm = (x-min(x))/(max(x)-min(x))
sc = MinMaxScaler(feature_range=(0, 1))
training_set_scaled = sc.fit_transform(training_set)

# Creating a data structure with 60 timesteps and 1 output
# 60 timesteps corresponds to 3 months of financial data
# For X_train: Column 0 is a day's stock price,
# following columns are the prices for the 60 days
# preceding the day represented by column 0
X_train = []
y_train = []
# range starts at the 60th day of the year
for i in range(60, 1258):
    X_train.append(training_set_scaled[i-60:i, 0])
    y_train.append(training_set_scaled[i, 0])
# convert to numpy arrays
X_train, y_train = np.array(X_train), np.array(y_train)

# Reshaping
# Input input dimensions for X_train tensor
# (number of observations, number of timesteps, number of indicators (Google stock price)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Part 2 - Building the RNN
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

# Initializing the RNN
regressor = Sequential()

# Adding the first LSTM layer and some Dropout regularisation
# Arg 1: Number of units (number of LSTM cells, or neurons)
# Arg 2: Return sequences (true)
# Arg 3: Input shape
regressor.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
# Arg: Rate at which neurons will drop. 20% in this case
regressor.add(Dropout(0.2))

# Second LSTM layer and Dropout regularisation
# Second layer doesn't require input shape because same unit size as first layer
regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(0.2))

# Third LSTM layer and Dropout regularisation
# Exactly the same as second layer
regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(0.2))

# Fourth LSTM layer and Dropout regularisation
# Final layer doesn't use return sequences
regressor.add(LSTM(units=50))
regressor.add(Dropout(0.2))

# Output layer
regressor.add(Dense(units=1))

# Compiling the RNN
# Compile with Adam stochastic gradient descent optimizer
# Loss is the mean squared error
regressor.compile(optimizer='adam', loss='mean_squared_error')

# Fitting the RNN to the Training set
# Parameters: Training sets X & y; number of epochs (training cycles); batch size
# Trained on 5 years of google stock prices
regressor.fit(X_train, y_train, epochs=100, batch_size=32)

# Making the predictions and visualising the results

# Getting the real stock price of 2017
dataset_test = pd.read_csv('Google_Stock_Price_Test.csv')
real_stock_price = dataset_test.iloc[:, 1:2].values

# Getting the predicted stock price of 2017
# Contains both training set and test set
# Horizontal concatenation (axis=0)
dataset_total = pd.concat((dataset_train['Open'], dataset_test['Open']), axis=0)
# Range of data
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)
X_test = []
# 20 financial days in test set
for i in range(60, 80):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_stock_price = regressor.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

# Visualising the results
plt.plot(real_stock_price, color='red', label='Real Google Stock Price')
plt.plot(predicted_stock_price, color='blue', label='Predicted Google Stock Price')
plt.title('Google Stock Price Predition')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')
plt.legend()
plt.show()