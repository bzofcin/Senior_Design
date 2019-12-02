import pandas as pd
import statistics as stat
import analytics
import os
import math
from sklearn.metrics import mean_squared_error

class Accuracy:
    def __init__(self, prediction_dir, stocks_dir):
        self.prediction_dir = prediction_dir
        self.stocks_dir = stocks_dir
        # print("in init")

    def single_epoch_method(self, prediction_dir, stocks_dir):
        prediction_sets = os.listdir(prediction_dir)
        actual_sets = os.listdir(stocks_dir)
        accuracy_sum = 0
        accuracy_set = []
        rmse_sum = 0
        rmse_set = []
        # print(actual_sets)
        # print(prediction_sets)

        # get dates to pull actual prices
        # get predicted prices
        real_set = 0
        for item in prediction_sets:
            # print(item)
            stock_name = item
            # print(stock_name)
            item = prediction_dir + item
            prediction_set = pd.read_csv(item)
            prediction_dates = prediction_set.iloc[:, 0]
            # print(prediction_dates)
            prediction_prices = prediction_set.iloc[:, 1]
            # print(prediction_prices)

            # get actual prices
            actual_file = stocks_dir + actual_sets[real_set]
            # print(actual_file)
            real_set += 1
            # print("Stock number " + str(real_set))
            actual_set = []
            actual_set = pd.read_csv(actual_file)
            starting_date = prediction_dates[0]
            num_days = len(prediction_dates)
            # num_days -= 1
            # print(actual_set)
            # print("Number of days: " + str(num_days))
            # print("Starting Date: " + str(starting_date))

            # starting_row: searches timestamp column for row containing specific date,
            #   in this case the first date in the predictions
            # .index[0] returns just the integer value of the row
            # print("Actual Prices: ")
            # print(actual_set)
            starting_row = actual_set.loc[actual_set['timestamp'] == starting_date].index[0]
            # print("Starting Row: " + str(starting_row))
            ending_row = starting_row + num_days
            # print("ending row: " + str(ending_row))
            # Column 4 contains closing price
            # print("starting price: " + str(actual_set.iloc[starting_row, 4]))
            # print("ending price: " + str(actual_set.iloc[ending_row, 4]))
            actual_prices = actual_set.iloc[starting_row:ending_row, 4]
            #actual_prices.reindex(index=actual_prices.index[::-1])
            # print("actual price: " + str(actual_prices))

            # prediction_prices.reindex(index=prediction_prices.index[::-1])
            predicted_stock_price = prediction_prices.tolist()
            real_stock_price = actual_prices.tolist()
            # print("Predicted: ")
            # print(predicted_stock_price)
            # print("Actual: ")
            # print(real_stock_price)
            analytics.rmse = self.calc_rmse(predicted_stock_price, real_stock_price, stock_name)
            print(stock_name + " RMSE: " + str(analytics.rmse))
            accuracy = self.accuracy_calc(predicted_stock_price, real_stock_price, stock_name)
            rmse_set.append(analytics.rmse)
            rmse_sum += analytics.rmse
            accuracy_set.append(accuracy)
            accuracy_sum += accuracy

        analytics.avg_accuracy = self.calc_avg(accuracy_sum, real_set)
        analytics.med_accuracy = self.calc_med(accuracy_set)
        analytics.hi_accuracy = self.calc_hi(accuracy_set)
        analytics.lo_accuracy = self.calc_lo(accuracy_set)
        analytics.var_accuracy = self.calc_var(accuracy_set)
        print("Accuracy Average: " + str(analytics.avg_accuracy))
        print("Accuracy Median: " + str(analytics.med_accuracy))
        print("Accuracy High: " + str(analytics.hi_accuracy))
        print("Accuracy Low: " + str(analytics.lo_accuracy))
        print("Accuracy Variance: " + str(analytics.var_accuracy))
        print(" ")
        analytics.avg_rmse = self.rmse_avg(rmse_sum, real_set)
        analytics.med_rmse = self.rmse_med(rmse_set)
        analytics.hi_rmse = self.rmse_hi(rmse_set)
        analytics.lo_rmse = self.rmse_lo(rmse_set)
        analytics.var_rmse = self.rmse_var(rmse_set)
        print("RMSE Average: " + str(analytics.avg_rmse))
        print("RMSE Median: " + str(analytics.med_rmse))
        print("RMSE High: " + str(analytics.hi_rmse))
        print("RMSE Low: " + str(analytics.lo_rmse))
        print("RMSE Variance: " + str(analytics.var_rmse))

    def accuracy_calc(self, predicted_stock_price, real_stock_price, stock_name):
        # Calculating accuracy
        predicted_length = len(predicted_stock_price)
        actual_length = len(real_stock_price)
        # print("predicted length: " + str(predicted_length))
        # print("actual length: " + str(actual_length))
        # trend up == 1; trend down == 0; no change == 2
        predicted_trend = 0
        real_trend = 0
        total = 0
        accurate = 0
        percent_accurate = 0
        for i in range(1, predicted_length):
            if predicted_stock_price[i] > predicted_stock_price[i - 1]:
                predicted_trend = 1
            elif predicted_stock_price[i] < predicted_stock_price[i - 1]:
                predicted_trend = 0
            elif predicted_stock_price[i] == predicted_stock_price[i - 1]:
                predicted_trend = 2

            if real_stock_price[i] > real_stock_price[i - 1]:
                real_trend = 1
            elif real_stock_price[i] < real_stock_price[i - 1]:
                real_trend = 0
            elif real_stock_price[i] == real_stock_price[i - 1]:
                real_trend = 2

            if predicted_trend == real_trend:
                accurate += 1

            total += 1

        percent_accurate = (accurate / total) * 100
        print(stock_name + " accuracy: " + str(percent_accurate) + "%")
        print(" ")
        return percent_accurate

    def calc_avg(self, accuracy_sum, real_set):
        return accuracy_sum / real_set

    def calc_med(self, accuracy_set):
        return stat.median(accuracy_set)

    def calc_hi(self, accuracy_set):
        return max(accuracy_set)

    def calc_lo(self, accuracy_set):
        return min(accuracy_set)

    def calc_var(self, accuracy_set):
        return stat.variance(accuracy_set)

    def calc_rmse(self, predicted_stock_price, real_stock_price, stock_name):
        min_price = min(real_stock_price)
        max_price = max(real_stock_price)
        price_range = max_price - min_price
        rmse = math.sqrt(mean_squared_error(real_stock_price, predicted_stock_price))
        rmse = (rmse/price_range)
        return rmse

    def rmse_avg(self, rmse_sum, real_set):
        return rmse_sum / real_set

    def rmse_med(self, rmse_set):
        return stat.median(rmse_set)

    def rmse_hi(self, rmse_set):
        return max(rmse_set)

    def rmse_lo(self, rmse_set):
        return min(rmse_set)

    def rmse_var(self, rmse_set):
        return stat.variance(rmse_set)

# stocks_dir = "../RNN_Experiments/Data Mining/Stock_Data_Indexed/"
# stocks_dir = "../Data Mining/Test_Data_Indexed/"
# prediction_dir = "../RNN_Experiments/Predicted_Data/E_10_PO_60_DP_30_H_5/"
# prediction_dir = "../RNN_Software/Prediction_Test/E_100_PO_60_DP_30_H_20/"

stocks_dir = "C:/Users/Terran/Documents/seniorprojectfall2019team7/RNN_Software/Automated_QA/Test_Data_Indexed/"
prediction_dir = "C:/Users/Terran/Documents/seniorprojectfall2019team7/RNN_Software/Prediction_Test/E_10_PO_60_DP_30_H_5/"
accuracy = Accuracy(prediction_dir, stocks_dir)
accuracy.single_epoch_method(prediction_dir, stocks_dir)

# accuracy = acc.Accuracy(FileDir, Stock_Dir)
# accuracy.single_epoch_method(FileDir, Stock_Dir)