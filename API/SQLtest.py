import csv

with open('../Data Mining/TestDir/Amazon.com Inc.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        row = (', '.join(row))
        print(row)