import mysql.connector


connection = mysql.connector.connect( host='unlvteamseven.mysql.pythonanywhere-services.com', user='unlvteamseven', passwd='Team7MySQL', db='unlvteamseven$aistockpickerdb' )
cursor = connection.cursor()

add_stocks = ("INSERT INTO stockData (id, timestamp, close, predicted) "
                "VALUES (%s, %s, %s, %s)"
                )

data = ('google', '2019-11-27', 1312.13, 1310.33);

cursor.execute(add_stocks, data)
connection.commit()

connection.close()
