import csv
import mysql.connector


connection = mysql.connector.connect( host='unlvteamseven.mysql.pythonanywhere-services.com', user='unlvteamseven', passwd='Team7MySQL', db='unlvteamseven$aistockpickerdb' )
cursor = connection.cursor()

cursor.execute("DELETE FROM stockData")
connection.commit()

with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            add_stocks = ("INSERT INTO stockData (id, timestamp, close, predicted) "
                "VALUES (%s, %s, %s, %s)"
                )
            data = (row[0], row[1], row[2], row[3])
            cursor.execute(add_stocks, data)
            connection.commit()
            line_count += 1
    print(f'Processed {line_count} lines.')
