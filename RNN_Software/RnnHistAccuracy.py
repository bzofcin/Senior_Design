import pandas as pd
import os


class Accuracy:
    def __init__(self, prediction_dir, stocks_dir):
        self.prediction_dir = prediction_dir
        self.stocks_dir = stocks_dir
        print("in init")

    def single_epoch_method(self, prediction_dir, stocks_dir):
        prediction_sets = os.listdir(prediction_dir)
        actual_sets = os.listdir(stocks_dir)
        prediction_array = []
        actual_array = []
        stock_names = []
        # print(actual_sets)
        # print(prediction_sets)

        # get dates to pull actual prices
        # get predicted prices
        i = 0
        for item in prediction_sets:
            # print(item)
            stock_names.append(item)
            item = prediction_dir + item
            print(item)
            prediction_set = pd.read_csv(item)
            prediction_dates = prediction_set.iloc[:, 0]
            # print(prediction_dates)
            prediction_prices = prediction_set.iloc[:, 1]
            # print(prediction_prices)
            prediction_array.append(prediction_prices)
            i += 1

        # get actual prices
        i = 0
        for item in actual_sets:
            item = stocks_dir + item
            actual_set = pd.read_csv(item)
            starting_date = prediction_dates[0]
            num_days = len(prediction_dates)
            num_days -= 1
            #print(actual_set)
            print("Number of days: " + str(num_days))
            print("Starting Date: " + str(starting_date))

            # starting_row: searches timestamp column for row containing specific date,
            #   in this case the first date in the predictions
            # .index[0] returns just the integer value of the row
            # !!!! For some reason this method returns a value 2 less than the row number
            #   when viewed in excel or pycharm !!!!
            # print("Actual Prices: ")
            # print(actual_set)
            starting_row = actual_set.loc[actual_set['timestamp'] == starting_date].index[0]
            print("Starting Row: " + str(starting_row))
            # num_days -= 3
            ending_row = starting_row + num_days + 1
            print("ending row: " + str(ending_row))
            # Column 4 contains closing price
            print("starting price: " + str(actual_set.iloc[starting_row, 4]))
            print("ending price: " + str(actual_set.iloc[ending_row, 4]))
            actual_prices = actual_set.iloc[starting_row:ending_row, 4]
            #actual_prices.reindex(index=actual_prices.index[::-1])
            # print("actual price: " + str(actual_prices))
            actual_array.append(actual_prices)
            i += 1

        # if os.path.exists(stocks_dir + "test.csv"):
        #     os.remove(stocks_dir + "test.csv")
        # with open(stocks_dir + "test.csv", "a") as fp:
        #     prediction_prices.to_csv(fp, index=True)

        # prediction_prices.reindex(index=prediction_prices.index[::-1])
        # testprice = prediction_prices.at[1, 1]
        # print("test: " + str(testprice))
        # predicted_stock_price = prediction_prices
        # real_stock_price = actual_prices
        predicted_stock_price = prediction_array
        real_stock_price = actual_array
        # print("Predicted: ")
        # print(predicted_stock_price)
        # print("Actual: ")
        # print(real_stock_price)
        self.many_epoch_method(predicted_stock_price, real_stock_price, stock_names)

    # takes arrays containing predicted and actual stock prices
    def many_epoch_method(self, predicted_stock_price, real_stock_price, stock_names):
        # Calculating accuracy
        i = 0
        for prediction in predicted_stock_price:
            actual = real_stock_price[i]
            print(actual)
            predicted_length = len(prediction)
            # trend up == 1; trend down == 0; no change == 2
            predicted_trend = 0
            real_trend = 0
            total = 0
            accurate = 0
            percent_accurate = 0
            for i in range(1, predicted_length):
                if prediction[i] > prediction[i - 1]:
                    predicted_trend = 1
                elif prediction[i] < prediction[i - 1]:
                    predicted_trend = 0
                elif prediction[i] == prediction[i - 1]:
                    predicted_trend = 2

                if actual[i] > actual[i - 1]:
                    real_trend = 1
                elif actual[i] < actual[i - 1]:
                    real_trend = 0
                elif actual[i] == actual[i - 1]:
                    real_trend = 2

                if predicted_trend == real_trend:
                    accurate += 1

                total += 1

            percent_accurate = (accurate / total) * 100
            print(stock_names[i] + " accuracy: " + str(percent_accurate) + "%")
            i += 1


# stocks_dir = "../RNN_Experiments/Data Mining/Stock_Data_Indexed/"
# stocks_dir = "../RNN_Experiments/Data Mining/TestDir/"
# prediction_dir = "../RNN_Experiments/Predicted_Data/E_1_PO_30_DP_1_H_5/"
stocks_dir = "../Data Mining/TestDir/"
prediction_dir = "../RNN_Software/Prediction_Test/E_1_PO_30_DP_1_H_5/"
accuracy = Accuracy(prediction_dir, stocks_dir)
accuracy.single_epoch_method(prediction_dir, stocks_dir)