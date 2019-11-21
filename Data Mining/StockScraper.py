from datetime import date, timedelta
import pandas_datareader.data as web
import  csv
import time

StockSym = {
"ATVI":	"Activision Blizzard Inc",
"ADBE":	"Adobe Inc.",
"AMD":	"Advanced Micro Devices Inc",
"ALGN":	"Align Technology Inc",
"ALXN":	"Alexion Pharmaceuticals Inc",
"AMZN":	"Amazon.com Inc",
"AMGN":	"Amgen Inc",
"AAL":	"American Airlines Group Inc",
"ADI":	"Analog Devices Inc",
"AAPL":	"Apple Inc",
"AMAT":	"Applied Materials Inc",
"ASML":	"ASML Holding NV",
"ADSK":	"Autodesk Inc",
"ADP":	"Automatic Data Processing Inc",
"AVGO":	"Broadcom Inc",
"BIDU":	"Baidu Inc",
"BIIB":	"Biogen Inc",
"BMRN":	"Biomarin Pharmaceutical Inc",
"CDNS":	"Cadence Design Systems Inc",
"CELG":	"Celgene Corp",
"CERN":	"Cerner Corp",
"CHKP":	"Check Point Software Technologies Ltd",
"CHTR":	"Charter Communications Inc",
"CTAS":	"Cintas Corp",
"CSCO":	"Cisco Systems Inc",
"CTXS":	"Citrix Systems Inc",
"CMCSA":"Comcast Corp",
"COST":	"Costco Wholesale Corp",
"CSX":	"CSX Corp",
"CTSH":	"Cognizant Technology Solutions Corp",
"DLTR":	"Dollar Tree Inc",
"EA":	"Electronic Arts",
"EBAY":	"eBay Inc",
"EXPE":	"Expedia Group Inc",
"FAST":	"Fastenal Co",
"FB":	"Facebook",
"FISV":	"Fiserv Inc",
"GILD":	"Gilead Sciences Inc",
"GOOG":	"Alphabet Class C",
"GOOGL":"Alphabet Class A",
"HAS":	"Hasbro Inc",
"HSIC":	"Henry Schein Inc",
"ILMN":	"Illumina Inc",
"INCY":	"Incyte Corp",
"INTC":	"Intel Corp",
"INTU":	"Intuit Inc",
"ISRG":	"Intuitive Surgical Inc",
"IDXX":	"IDEXX Laboratories Inc",
"^IXIC": "NASDAQ Composite",
"JBHT":	"J.B. Hunt Transport Services Inc",
"JD":	"JD.com Inc",
"KLAC":	"KLA Corp",
"KHC":	"Kraft Heinz Co",
"LRCX":	"Lam Research Corp",
"LBTYK":"Liberty Global PLC",
"LULU":	"Lululemon Athletica Inc",
"MELI":	"Mercadolibre Inc",
"MAR":	"Marriott International Inc",
"MCHP":	"Microchip Technology Inc",
"MDLZ":	"Mondelez International Inc",
"MNST":	"Monster Beverage Corp",
"MSFT":	"Microsoft Corp",
"MU":	"Micron Technology Inc",
"MXIM":	"Maxim Integrated Products Inc",
"MYL":	"Mylan NV",
"NTAP":	"NetApp Inc",
"NFLX":	"Netflix Inc",
"NTES":	"NetEase Inc",
"NVDA":	"NVIDIA Corp",
"NXPI":	"NXP Semiconductors NV",
"ORLY":	"O'Reilly Automotive Inc",
"PAYX":	"Paychex Inc",
"BKNG":	"Booking Holdings Inc",
"PYPL":	"PayPal Holdings Inc",
"PEP":	"PepsiCo Inc.",
"QCOM":	"Qualcomm Inc",
"REGN":	"Regeneron Pharmaceuticals Inc",
"ROST":	"Ross Stores Inc",
"SIRI":	"Sirius XM Holdings Inc",
"SWKS":	"Skyworks Solutions Inc",
"SBUX":	"Starbucks Corp",
"SNPS":	"Synopsys Inc",
"TTWO":	"Take-Two Interactive Software Inc",
"TSLA":	"Tesla Inc",
"TXN":	"Texas Instruments Inc",
"TMUS":	"T-Mobile US Inc",
"ULTA":	"Ulta Beauty Inc",
"UAL":	"United Airlines Holdings Inc",
"VRSN":	"Verisign Inc",
"VRSK":	"Verisk Analytics Inc",
"VRTX":	"Vertex Pharmaceuticals Inc",
"WBA":	"Walgreens Boots Alliance Inc",
"WDC":	"Western Digital Corp",
"WDAY":	"Workday Inc",
"WYNN":	"Wynn Resorts Ltd",
"XEL":	"Xcel Energy Inc",
"XLNX":	"Xilinx Inc"
}


StartTime = time.time()
Today = date.today()
Yesterday = Today - timedelta(days = 16)

for item in StockSym:
    try:
        df = web.DataReader(item, 'yahoo', Yesterday, Yesterday)
        FormatedDate = Yesterday.strftime("%Y-%m-%d")
        for index, rows in df.iterrows():
            MyList = [FormatedDate, rows[0], rows[1], rows[2], rows[3], rows[4]]

        with open("./Stock_Data/" + StockSym.get(item) + ".csv", "a") as fp:
            wr = csv.writer(fp, dialect = 'excel')
            wr.writerow(MyList)
    except:
        try:
            df = web.DataReader(item, 'google', Yesterday, Yesterday)
            FormatedDate = Yesterday.strftime("%Y-%m-%d")
            for index, rows in df.iterrows():
                MyList = [FormatedDate, rows[0], rows[1], rows[2], rows[3], rows[4]]

            with open("./Stock_Data/" + StockSym.get(item) + ".csv", "a") as fp:
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(MyList)
        except:
            print(StockSym.get(item) + " was not reached\n")

print("--- %s seconds ---" % (time.time() - StartTime))
print("Data has been collected succesfully")
