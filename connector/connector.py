import csv
import mysql.connector


Stocks = {
"Amazon.com Inc",
"Apple Inc",
"Biogen Inc",
"Booking Holdings Inc",
"Celgene Corp",
"Cisco Systems Inc",
"Costco Wholesale Corp",
"Microsoft Corp",
"NVIDIA Corp",
"eBay Inc"
}

connection = mysql.connector.connect( host='unlvteamseven.mysql.pythonanywhere-services.com', user='unlvteamseven', passwd='Team7MySQL', db='unlvteamseven$aistockpickerdb' )
cursor = connection.cursor()

cursor.execute("DELETE FROM stockpicker_predictions")
connection.commit()

idNo = 1

for file in Stocks:
    with open('/home/unlvteamseven/aistockpicker/static/predictions/' + file + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0 or line_count % 2 == 1:
                line_count += 1
            else:
                add_stocks = ("INSERT INTO stockpicker_predictions (id, stockname, timestamp, close, prediction) "
                    "VALUES (%s, %s, %s, %s, %s)"
                    )
                data = (idNo, row[0], row[1][0:4] + ',' + row[1][5:7] + ',' + row[1][8:], row[2], row[3])
                cursor.execute(add_stocks, data)
                connection.commit()
                line_count += 1
                idNo += 1
                print(idNo)
        print(f'Processed {line_count} lines.')

connection.close()
