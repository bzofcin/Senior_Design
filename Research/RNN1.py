# RNN to predict the sequence of a sine wave.

import math
import numpy as np
import matplotlib.pyplot as plt

# Input: single sequence of length 50 (the sine wave)
sin_wave = np.array([math.sin(x) for x in np.arange(200)])
plt.plot(sin_wave[:50])

X = []
Y = []

# Shape of input data: (number_of_records x length_of_sequence x types_of_sequences)
# Only 1 type of sequence: sine wave
# Shape of output data: (number_of_records x types_of_sequences)
# Where types_of_sequences is 1

# Length of sequence = 50
seq_len = 50
# num_records is unpredicted portion of the sequence
num_records = len(sin_wave) - seq_len

# Create lists X and Y, input and output respectively
# num_records - 50 because we set aside 50 records for validation data (see below)
for i in range(num_records - 50):
    # Returns 50 records from sin_wave in each array entry (2D array)
    X.append(sin_wave[i:i + seq_len])
    # Returns next consecutive record for output
    Y.append(sin_wave[i + seq_len])

# Convert input list X into a numpy array
# Reshape X array dimensions to be 100 x 50 x 1 or
# (number_of_records x length_of_sequence x types_of_sequences)
X = np.array(X)
X = np.expand_dims(X, axis=2)

# Convert output list Y into a numpy array
# Reshape Y array dimensions to be 100 x 1 or
# (number_of_records x types_of_sequences)
Y = np.array(Y)
Y = np.expand_dims(Y, axis=1)

# Print shape of the data
print("X.shape: " + str(X.shape))
print("Y.shape: " + str(Y.shape))

# 50 records set aside for validation data, created here:
X_val = []
Y_val = []

# Create lists X and Y for input/output validation data
# Consists of remaining 50 records left out of input/output data
for i in range(num_records - 50, num_records):
    X_val.append(sin_wave[i:i + seq_len])
    Y_val.append(sin_wave[i + seq_len])

X_val = np.array(X_val)
X_val = np.expand_dims(X_val, axis=2)

Y_val = np.array(Y_val)
Y_val = np.expand_dims(Y_val, axis=1)

# Create RNN architecture
# Consists of input sequence, 100-unit hidden layer, and a single valued output

learning_rate = 0.0001
# number of epochs
nepoch = 25
# length of (input?) sequence
T = 50
# Units in hidden layer
hidden_dim = 100
# Units in output layer
output_dim = 1

# Backpropagation Through Time Truncation
bptt_truncate = 5
# Gradient clipping, avoids exploding gradient
min_clip_value = -10
max_clip_value = 10

# Initialize weights to random values
# U is weight matrix between input and hidden layers
U = np.random.uniform(0, 1, (hidden_dim, T))
# W is weight matrix for shared weights in the Hidden Layer
W = np.random.uniform(0, 1, (hidden_dim, hidden_dim))
# V is the weight matrix between hidden and output layers
V = np.random.uniform(0, 1, (output_dim, hidden_dim))

# Activation Function (sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


for epoch in range(nepoch):
    # check loss on train
    loss = 0.0

    # do a forward pass to get prediction
    for i in range(Y.shape[0]):
        x, y = X[i], Y[i]  # get input, output values of each record
        prev_s = np.zeros((hidden_dim,
                           1))  # here, prev-s is the value of the previous activation of hidden layer; which is initialized as all zeroes
        for t in range(T):
            new_input = np.zeros(x.shape)  # we then do a forward pass for every timestep in the sequence
            new_input[t] = x[t]  # for this, we define a single input for that timestep
            mulu = np.dot(U, new_input)
            mulw = np.dot(W, prev_s)
            add = mulw + mulu
            s = sigmoid(add)
            mulv = np.dot(V, s)
            prev_s = s

        # calculate error
        loss_per_record = (y - mulv) ** 2 / 2
        loss += loss_per_record
    loss = loss / float(y.shape[0])

    # check loss on val
    val_loss = 0.0
    for i in range(Y_val.shape[0]):
        x, y = X_val[i], Y_val[i]
        prev_s = np.zeros((hidden_dim, 1))
        for t in range(T):
            new_input = np.zeros(x.shape)
            new_input[t] = x[t]
            mulu = np.dot(U, new_input)
            mulw = np.dot(W, prev_s)
            add = mulw + mulu
            s = sigmoid(add)
            mulv = np.dot(V, s)
            prev_s = s

        loss_per_record = (y - mulv)**2 / 2
        val_loss += loss_per_record
    val_loss = val_loss / float(y.shape[0])

    print('Epoch: ', epoch + 1, ', Loss: ', loss, ', Val Loss: ', val_loss)

    # train model
    for i in range(Y.shape[0]):
        x, y = X[i], Y[i]

        layers = []
        prev_s = np.zeros((hidden_dim, 1))
        dU = np.zeros(U.shape)
        dV = np.zeros(V.shape)
        dW = np.zeros(W.shape)

        dU_t = np.zeros(U.shape)
        dV_t = np.zeros(V.shape)
        dW_t = np.zeros(W.shape)

        dU_i = np.zeros(U.shape)
        dW_i = np.zeros(W.shape)

        # forward pass
        for t in range(T):
            new_input = np.zeros(x.shape)
            new_input[t] = x[t]
            mulu = np.dot(U, new_input)
            mulw = np.dot(W, prev_s)
            add = mulw + mulu
            s = sigmoid(add)
            mulv = np.dot(V, s)
            layers.append({'s': s, 'prev_s': prev_s})
            prev_s = s

        # derivative of pred
        dmulv = (mulv - y)

        # backward pass
        for t in range(T):
            dV_t = np.dot(dmulv, np.transpose(layers[t]['s']))
            dsv = np.dot(np.transpose(V), dmulv)

            ds = dsv
            dadd = add * (1 - add) * ds

            dmulw = dadd * np.ones_like(mulw)

            dprev_s = np.dot(np.transpose(W), dmulw)

            for i in range(t - 1, max(-1, t - bptt_truncate - 1), -1):
                ds = dsv + dprev_s
                dadd = add * (1 - add) * ds

                dmulw = dadd * np.ones_like(mulw)
                dmulu = dadd * np.ones_like(mulu)

                dW_i = np.dot(W, layers[t]['prev_s'])
                dprev_s = np.dot(np.transpose(W), dmulw)

                new_input = np.zeros(x.shape)
                new_input[t] = x[t]
                dU_i = np.dot(U, new_input)
                dx = np.dot(np.transpose(U), dmulu)

                dU_t += dU_i
                dW_t += dW_i

            dV += dV_t
            dU += dU_t
            dW += dW_t

            if dU.max() > max_clip_value:
                dU[dU > max_clip_value] = max_clip_value
            if dV.max() > max_clip_value:
                dV[dV > max_clip_value] = max_clip_value
            if dW.max() > max_clip_value:
                dW[dW > max_clip_value] = max_clip_value

            if dU.min() < min_clip_value:
                dU[dU < min_clip_value] = min_clip_value
            if dV.min() < min_clip_value:
                dV[dV < min_clip_value] = min_clip_value
            if dW.min() < min_clip_value:
                dW[dW < min_clip_value] = min_clip_value

        # update
        U -= learning_rate * dU
        V -= learning_rate * dV
        W -= learning_rate * dW

preds = []
for i in range(Y.shape[0]):
    x, y = X[i], Y[i]
    prev_s = np.zeros((hidden_dim, 1))
    # Forward pass
    for t in range(T):
        mulu = np.dot(U, x)
        mulw = np.dot(W, prev_s)
        add = mulw + mulu
        s = sigmoid(add)
        mulv = np.dot(V, s)
        prev_s = s

    preds.append(mulv)

preds = np.array(preds)

plt.plot(preds[:, 0, 0], 'g')
plt.plot(Y[:, 0], 'r')
plt.show()

preds = []
for i in range(Y_val.shape[0]):
    x, y = X_val[i], Y_val[i]
    prev_s = np.zeros((hidden_dim, 1))
    # For each time step...
    for t in range(T):
        mulu = np.dot(U, x)
        mulw = np.dot(W, prev_s)
        add = mulw + mulu
        s = sigmoid(add)
        mulv = np.dot(V, s)
        prev_s = s

    preds.append(mulv)

preds = np.array(preds)

plt.plot(preds[:, 0, 0], 'g')
plt.plot(Y_val[:, 0], 'r')
plt.show()

# from sklearn.metrics import mean_squared_error
#
# math.sqrt(mean_squared_error(Y_val[:, 0] * max_val, preds[:, 0, 0] * max_val))