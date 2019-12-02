import pandas as pd
import os
import csv

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

StockSym1 = {
"AMD":	"Advanced Micro Devices Inc",
"AMZN":	"Amazon.com Inc",
"AMGN":	"Amgen Inc",
"AAPL":	"Apple Inc",
"BIIB":	"Biogen Inc",
"BKNG":	"Booking Holdings Inc",
"CELG":	"Celgene Corp",
"COST":	"Costco Wholesale Corp",
"MSFT":	"Microsoft Corp",
"NVDA":	"NVIDIA Corp"
}

# data_dir = "../Data Mining/Stock_Data/"
data_dir = "../Data Mining/TestDir/"
# indexed_dir = "../Data Mining/Stock_Data_Indexed/"
indexed_dir = "../Data Mining/Test_Data_Indexed/"
reversed_dir = "../Data Mining/Stock_Data_Reversed/"
if not os.path.exists(indexed_dir):
    os.mkdir(indexed_dir)
if not os.path.exists(reversed_dir):
    os.mkdir(reversed_dir)

for item in StockSym1:
    # Reverse index
    file = data_dir + StockSym1.get(item) + ".csv"
    df = pd.read_csv(file)
    # print(datasheet)
    # datasheet.reindex(index=datasheet.index[::-1])
    reversed_df = df.iloc[::-1]
    # print(reversed_df)
    # Save data frame to excel file
    # indexed_df = reversed_df.iloc[:, 1:]
    if os.path.exists(reversed_dir + StockSym1.get(item) + ".csv"):
        os.remove(reversed_dir + StockSym1.get(item) + ".csv")
    with open(reversed_dir + StockSym1.get(item) + ".csv", "a") as fp:
        reversed_df.to_csv(fp)

    # test = pd.read_csv(indexed_dir + StockSym1.get(item) + ".csv")
    # print(test)


    # Load excel file to remove new reversed index column
    file = reversed_dir + StockSym1.get(item) + ".csv"
    df = pd.read_csv(file)
    # print(df)
    indexed_df = df.iloc[:, 1:]
    print(indexed_df)

    if os.path.exists(indexed_dir + StockSym1.get(item) + ".csv"):
        os.remove(indexed_dir + StockSym1.get(item) + ".csv")
    with open(indexed_dir + StockSym1.get(item) + ".csv", "a") as fp:
        indexed_df.to_csv(fp, index=False)

    # test = pd.read_csv(indexed_dir + StockSym1.get(item) + ".csv")
    # print(test)

if os.path.exists(reversed_dir):
    os.remove(reversed_dir)
    print(reversed_dir + " is removed.")