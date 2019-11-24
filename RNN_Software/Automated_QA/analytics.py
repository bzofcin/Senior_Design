import RnnHistAccuracy as acc
import RnnHistRuntime as rt
import pandas as pd
import os


class Analytics:
    def __init__(self, epochs, predict_on, days_predicted, history):
        self.epochs = epochs
        self.predict_on = predict_on
        self.days_predicted = days_predicted
        self.history = history

        self.avg_accuracy = 0
        self.med_accuracy = 0
        self.hi_accuracy = 0
        self.lo_accuracy = 0

        self.avg_epochRT = 0
        self.med_epochRT = 0
        self.high_epochRT = 0
        self.low_epochRT = 0
        self.total_runtime = 0

        self.volume = 0


    def accuracy(self, stocks_dir, prediction_dir):
        accuracy = acc(prediction_dir, stocks_dir)
        accuracy.single_epoch_method(prediction_dir, stocks_dir)

    def runtime(self, start_time):
        pass
