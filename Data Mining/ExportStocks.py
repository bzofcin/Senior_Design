import urllib.request
import time
import os
import sys

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
"CTRP":	"Ctrip.Com International Ltd",
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
"PCAR":	"Paccar Inc",
"BKNG":	"Booking Holdings Inc",
"PYPL":	"PayPal Holdings Inc",
"PEP":	"PepsiCo Inc.",
"QCOM":	"Qualcomm Inc",
"REGN":	"Regeneron Pharmaceuticals Inc",
"ROST":	"Ross Stores Inc",
"SIRI":	"Sirius XM Holdings Inc",
"SWKS":	"Skyworks Solutions Inc",
"SBUX":	"Starbucks Corp",
"SYMC":	"Symantec Corp",
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


def DownloadFiles(symbol, name):
#Downloads the files from Alphavantage and stores them in a file called Stock_Data

    Front ="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="
    Back = "&outputsize=full&apikey=FI97CUETTHW9CX8Q&datatype=csv"
    urllib.request.urlretrieve(Front + symbol + Back, "Stock_Data/" + name.get(symbol) + ".csv")

def Create():
#Checks to see if the Stock_Data File exists
#if it does it moves on, if it doesn't then creates the file location
    CanCreate = "Stock_Data"

    print ("Verifying required files and directories...")
    if os.path.exists(CanCreate) is False:
    	print (CanCreate + "/ Doesn't exist, creating it...")
    	os.mkdir(CanCreate)

    print ("Verification passed\n")


if __name__ == "__main__":
#calls function to create file location then stores files into Stock_Data
#Only 5 files can be downloaded per minute, so time.sleep(13) pauses the next files
#for 13 seconds. Currently 30 files are being downloaded per day which takes 6 minutes
#to complete 

    Create()

    for item in StockSym:
        DownloadFiles(item, StockSym)
        time.sleep(13)

    sys.exit(0)
