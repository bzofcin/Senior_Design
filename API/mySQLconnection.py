import mysql.connector
import sshtunnel
import csv

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='unlvteamseven', ssh_password='Unlv#2019',
    remote_bind_address=('unlvteamseven.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = mysql.connector.connect(
        user='unlvteamseven', password='Team7MySQL',
        host='127.0.0.1', port=tunnel.local_bind_port,
        database='unlvteamseven$aistockpickerdb',
    )

    DB_NAME = 'delphi_AI'

    TABLES = {}
    TABLES['prediction'] = (
        "CREATE TABLE 'prediction' ("
        "  'stockname' varchar(40) NOT NULL"
        "  'timestamp' date NOT NULL,"
        "  'open' float(7,4) NOT NULL,"
        "  'high' float(7,4) NOT NULL,"
        "  'low' float(7,4) NOT NULL,"
        "  'close' float(7,4) NOT NULL,"
        "  'volume' int(11) NOT NULL,"
        "  PRIMARY KEY ('stockname', 'timestamp')"
        ") ENGINE=InnoDB"
    )

    cursor = connection.cursor()
    try:
        with open('../Data Mining/TestDir/Amazon.com Inc.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', header=False)
            sql = "INSERT INTO prediction (stockname) VALUES (%s)"
            for row in csv_reader:
                row = (', '.join(row))
                print(row)
                cursor.execute(sql, row)
    except:
        print("exception")
        connection.rollback()

connection.close()