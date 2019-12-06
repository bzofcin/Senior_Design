import csv
import mysql.connector


Stocks = {
"Activision Blizzard Inc",
"Advanced Micro Devices Inc",
"Alphabet Class A",
"Alphabet Class C",
"American Airlines Group Inc",
"Analog Devices Inc",
"Baidu Inc",
"Biomarin Pharmaceutical Inc",
"Broadcom Inc",
"CSX Corp",
"Cadence Design Systems Inc",
"Cerner Corp",
"Charter Communications Inc",
"Cintas Corp",
"Citrix Systems Inc",
"Cognizant Technology Solutions Corp",
"Ctrip.Com International Ltd",
"Dollar Tree Inc",
"Expedia Group Inc",
"Facebook",
"Fastenal Co",
"Hasbro Inc",
"IDEXX Laboratories Inc",
"Illumina Inc",
"Intuitive Surgical Inc",
"J.B. Hunt Transport Services Inc",
"JD.com Inc",
"Kraft Heinz Co",
"Liberty Global PLC",
"Lululemon Athletica Inc",
"Maxim Integrated Products Inc",
"Mercadolibre Inc",
"Microchip Technology Inc",
"Micron Technology Inc",
"Mondelez International Inc",
"Monster Beverage Corp",
"Mylan NV",
"NXP Semiconductors NV",
"NetApp Inc",
"NetEase Inc",
"Paccar Inc",
"PayPal Holdings Inc",
"Ross Stores Inc",
"Sirius XM Holdings Inc",
"Skyworks Solutions Inc",
"Synopsys Inc",
"T-Mobile US Inc",
"Take-Two Interactive Software Inc",
"Ulta Beauty Inc",
"United Airlines Holdings Inc",
"Verisign Inc",
"Verisk Analytics Inc",
"Walgreens Boots Alliance Inc",
"Western Digital Corp",
"Workday Inc",
"Wynn Resorts Ltd",
"Xcel Energy Inc",
"Xilinx Inc",
"Amazon.com Inc",
"ASML Holding NV",
"Adobe Inc.",
"Alexion Pharmaceuticals Inc",
"Align Technology Inc",
"Applied Materials Inc",
"Autodesk Inc",
"Automatic Data Processing Inc",
"Check Point Software Technologies Ltd",
"Comcast Corp",
"Electronic Arts",
"Fiserv Inc",
"Gilead Sciences Inc",
"Henry Schein Inc",
"Incyte Corp",
"Intel Corp",
"Intuit Inc",
"KLA Corp",
"Lam Research Corp",
"Marriott International Inc",
"Netflix Inc",
"O'Reilly Automotive Inc",
"PepsiCo Inc.",
"Qualcomm Inc",
"Regeneron Pharmaceuticals Inc",
"Starbucks Corp",
"Symantec Corp",
"Tesla Inc",
"Texas Instruments Inc",
"Biogen Inc",
"Booking Holdings Inc",
"Celgene Corp",
"Cisco Systems Inc",
"Costco Wholesale Corp",
"Microsoft Corp",
"NVIDIA Corp",
"eBay Inc",
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
