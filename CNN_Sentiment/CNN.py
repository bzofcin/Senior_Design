import tensorflow as tf
import numpy as np

class TextCNN(object):
    # sequence_length: Length of sequences. Sentences are all padded to have the same length (59 words).
    # num_classes: Number classes in output layer (2: positive and negative).
    # vocab_size: Size of vocabulary. Defines size of our embedding layer with shape [vocab_size, embedding_size].
    # embedding_size: Dimensionality of embeddings
    # filter_sizes: The number of words our convolutional filters will cover. We wlil have num_filters
    #   for each size specified here. eg, [3, 4, 5] means we will have filters that slide over
    #   3, 4 and 5 words respectively, for a total of (3 * num_filters) filters.
    # num_filters: The number of filters per filter size (see above).
    def __init__(self, sequence_length, num_classes, vocab_size,
                 embedding_size, filter_sizes, num_filters):
        # Placeholders for input, output and dropout.
        # tf.placeholder creates a placeholder variable tha twe feed t the network, then execute at train or test time
        # Second arg is the shape of the input tensor
        # "None" means that the length of that dimension could be anything
        # In our case, the first dimension is the batch size. Using none allows the network
        #   to handle arbitrary batch sizes.
        self.input_x = tf.placeholder(tf.int32, [None, sequence_length], name="input_x")
        self.input_y = tf.placeholder(tf.float32, [None, num_classes], name="input_y")
        self.dropout_keep_prob = tf.placeholder(tf.float32, name="droput_keep_prob")

        # Embedding Layer
        # The first layer is the embedding layer
        # It maps vocab word indices into low-dimensional vector representations.
        # Essentially a lookup table we learn from the data
        # 'tf.device("/cpu:0") forces operations on CPU. Tensorflow defaults to GPU otherwise.
        #   Embedding implementation currently isn't supported for GPU and throws an error
        # 'tf.name_scope' creats a new Name Scope with the name "embedding".
        #   Adds all operations into a top-level node for a nice hierarchy when visualizing network
        #   on tensorboard.
        with tf.device('/cpu:0'), tf.name_scope("embedding"):
            # 'W' is our embedding matrix that we learn during training.
            W = tf.Variable(
                tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0), name="W"
            )
            self.embedded_chars = tf.nn.embedding_lookup(W, self.input_x)
            self.embedded_chars_expanded = tf.expand_dims(self.embedded_chars, -1)

        # Create a convolution + maxpool layer for each filter size
        pooled_outputs = []
        for i, filter_size in enumerate(filter_sizes):
            with tf.name_scope("conv-maxpools-%s" % filter_size):
                # Convolution Layer
                filter_shape = [filter_size, embedding_size, 1, num_filters]
                W = tf.Variable(tf.truncated_normal(filter_shape, stddev=0.1))