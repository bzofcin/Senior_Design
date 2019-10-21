# Recurrent Neural Network

# Import data set paths
#from data_path import *
import data_path as p

# Runtime timer
import time

start_time = time.time()


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the training set
#only numpy arrays can be input arrays for keras 
dataset_train = pd.read_csv('Amazon.com Inc.csv')
# this is training on the first opening price
# need to end range at n+1 because the uperbound is excluded  
# [:] gets entire column
#.values creats a numpy array 
training_set = dataset_train.iloc[:, 1:2].values

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
# using normalization function norm = ( x - min(x)) / ( max(x) - min(x) ) will output all new scale stock prices between 0 and one 
sc = MinMaxScaler(feature_range = (0, 1))
# this will get the scaling set and fit meaning it wil get the min stock price and max to be able to apply it to the normalization formula 
#transform will run each stock price in the traing set through the function and evaluate
#training_set must be passed as an arg to run the correct values to be evaluated
#then it is placed in the training_set_scaled array 
training_set_scaled = sc.fit_transform(training_set)

# Creating a data structure with 60 timesteps and 1 output
#at each time t the rnn is going to look at each 60 
#time steps 
#holds the input of the neural net. the previous 60 days. 
X_train = []
#holds the output of the neural net the next financial day 
y_train = []
#populates x and y train have to start teh loop from the n day out that is being used
#so the range is from the 90 day to 1258 to make sure there is no array out of bounds 

for i in range(60, 5010):
    # appends the previouse n days of stock prices up to i to a list 
    #used for memorizing the previous n days to predict the n+1 day price
    # the 0 is the column from training x scaled
    # will ghave to add more when using more stocks to evaluate 
    X_train.append(training_set_scaled[i-60:i, 0])
    # will hold i stock price
    y_train.append(training_set_scaled[i, 0])
    #creates the numpy array holding the xtrain and y train data 
X_train, y_train = np.array(X_train), np.array(y_train)

# Reshaping
#adding dementions to the data structure. this where more predictors can be added to the array such as close price, or other stocks 
# (the batch size, the time steps. and the number of sets used to predict) 
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))



# Part 2 - Building the RNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

# Initialising the RNN
regressor = Sequential()

# Adding the first LSTM layer and some Dropout regularisation
#drop out is used for over filling 
#three args number of units or cells that will be used 
#return sequence needs to be true until you are done stacking layers 
regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
#20% of ther neurons will be dropped out. this  means that 10 cells wil be ignored out of 50 
regressor.add(Dropout(0.2))
#dont need to speciy input shape it is alredy specified 
# Adding a second LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

# Adding a third LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

# Adding a fourth LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))

# Adding the output layer
#fully connected layer using dnese class 
#same at ann
#number of neurons needed to be in the output layer. 
#the unit correstponds to the number of neurons that need to be in the oupout layer
#this is based off the dimension of the ouput which is 1
regressor.add(Dense(units = 1))

# Compiling the RNN
#adam optimizer look up what it means 
#using mean squared for loss function 
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Fitting the RNN to the Training set
#this fits the information to the training set 
#first input is the training set and ouptut of prediction which is compared to ytrain
#the next inout is the y train which is the comparison of the 
#batch size is the size of batch going into 
regressor.fit(X_train, y_train, epochs = 100, batch_size = 100)



# Part 3 - Making the predictions and visualising the results

# Getting the real stock price of 2017
#model does not capture spike only trends 
dataset_test = pd.read_csv('amazontest.csv')
real_stock_price = dataset_test.iloc[:, 1:2].values

# Getting the predicted stock price of 2017
dataset_total = pd.concat((dataset_train['open'], dataset_test['open']), axis = 0)
#gets the first - the data set to  - 60 to find the info to predict t+1
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
inputs = inputs.reshape(-1,1)
#scaled the inputs 
inputs = sc.transform(inputs)
X_test = []
#info foroutput the 60 days past to predict the next 20 days. 
for i in range(60, 80):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
#this returns the predictions and store in a new var
predicted_stock_price = regressor.predict(X_test)
#get original scale of predicted values 
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

# Visualising the results
plt.plot(real_stock_price, color = 'red', label = 'Real Amazon Stock Price')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted Amazon Stock Price')
plt.title('Amazon Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Amazon Stock Price')
plt.legend()
plt.show()

# Output runtime
print("--- %s seconds ---" % (time.time() - start_time))
