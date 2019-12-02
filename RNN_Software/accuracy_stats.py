

def calculate_accuracy(predicted_stock_price, real_stock_price, testname):
    # Calculating accuracy
    predicted_length = len(predicted_stock_price)
    # trend up == 1; trend down == 0; no change == 2
    predicted_trend = 0
    real_trend = 0
    total = 0
    accurate = 0
    percent_accurate = 0
    for i in range(1, predicted_length):
        if predicted_stock_price[i] > predicted_stock_price[i-1]:
            predicted_trend = 1
        elif predicted_stock_price[i] < predicted_stock_price[i-1]:
            predicted_trend = 0
        elif predicted_stock_price[i] == predicted_stock_price[i-1]:
            predicted_trend = 2

        if real_stock_price[i] > real_stock_price[i-1]:
            real_trend = 1
        elif real_stock_price[i] < real_stock_price[i-1]:
            real_trend = 0
        elif real_stock_price[i] == real_stock_price[i-1]:
            real_trend = 2

        if predicted_trend == real_trend:
            accurate += 1

        total += 1

    percent_accurate = (accurate/total) * 100
    print("Accuracy: " + str(percent_accurate) + "%" + testname)
