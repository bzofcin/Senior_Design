import numpy as np

# creating the input array
X = np.array([[1, 0, 1, 0], [1, 0, 1, 1], [0, 1, 0, 1]])
print('\n Input:')
print(X)

# creating the output array
y = np.array([[1], [1], [0]])
print('\n Actual Output:')
print(y)


# defining the Sigmoid Function
def sigmoid(x):
    return 1/(1 + np.exp(-x))


# derivative of Sigmoid Function
def derivatives_sigmoid(x):
    return x * (1 - x)


# initializing the variables
# number of training iterations
epoch = 5000
# learning rate
lr = 0.1
# number of features in data set
inputlayer_neurons = X.shape[1]
# number of hidden layers neurons
hiddenlayer_neurons = 3
# number of neurons at output layer
output_neurons = 1

# initializing weight and bias
# weights matrix
wh = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))
# bias array
bh = np.random.uniform(size=(1, hiddenlayer_neurons))
# output array
wout = np.random.uniform(size=(hiddenlayer_neurons, output_neurons))
# output bias array
bout = np.random.uniform(size=(1, output_neurons))

# training the model
for i in range(epoch):

    # Forward Propogation
    # Dot product of input and weight matrices
    hidden_layer_input1 = np.dot(X, wh)
    # Add bias units to neurons
    hidden_layer_input = hidden_layer_input1 + bh
    # Activation function (sigmoid); non-linear transformation
    hiddenlayer_activations = sigmoid(hidden_layer_input)
    # Dot product of weights and output neurons
    output_layer_input1 = np.dot(hiddenlayer_activations, wout)
    # Add bias units to output neurons
    output_layer_input = output_layer_input1 + bout
    # Activation function for output nodes
    output = sigmoid(output_layer_input)

    # Back-propagation
    # Calculate loss
    E = y-output
    # Compute gradient of output using derivative of sigmoid
    slope_output_layer = derivatives_sigmoid(output)
    # Compute gradient of hidden neurons similarly
    slope_hidden_layer = derivatives_sigmoid(hiddenlayer_activations)
    # Compute DELTA (change factor) of output layer
    d_output = E * slope_output_layer
    # Error propagates back from output to hidden layer
    # Dot product of output delta with eights of edges
    # between hidden and output layer.
    # wout.T means wout is transposed
    Error_at_hidden_layer = d_output.dot(wout.T)
    # Compute delta for hidden layer:
    # Multiply hidden layer error by hidden layer gradient
    d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
    wout += hiddenlayer_activations.T.dot(d_output) * lr
    bout += np.sum(d_output, axis=0, keepdims=True) * lr
    wh += X.T.dot(d_hiddenlayer) * lr
    bh += np.sum(d_hiddenlayer, axis=0, keepdims=True) * lr

print('\n Output from the model:')
print(output)
