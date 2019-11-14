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
        self.input_x = tf.placeholder(tf.int32, [None, sequence_length], name="input_x")