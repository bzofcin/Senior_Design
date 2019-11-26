import RnnHistAccuracy as acc
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
        self.var_accuracy = 0

        self.rmse = 0

        self.avg_rmse = 0
        self.med_rmse = 0
        self.hi_rmse = 0
        self.low_rmse = 0
        self.var_rmse = 0

        # self.avg_epochRT = 0
        # self.med_epochRT = 0
        # self.high_epochRT = 0
        # self.low_epochRT = 0
        # self.total_runtime = 0

        self.volume = 0

    def get_dir(self, ):
        pass

    def calc_accuracy(self, stocks_dir, prediction_dir):
        accuracy = acc(prediction_dir, stocks_dir)
        accuracy.single_epoch_method(prediction_dir, stocks_dir)