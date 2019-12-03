import pandas as pd
import plotly.graph_objects as go
import DirectoryInfo as di
import matplotlib.pyplot as plt


df = pd.read_csv('Processed_Data/Apple Inc/Apple Inc_Epoch_100.csv')
df = di.ResetDataStockData(df, True)

plt.plot( 'timestamp', 'Actual Close', data=df, marker='', color='red')
plt.plot( 'timestamp', 'Predicted Close', data=df, marker='', color='blue')

plt.legend()
plt.show()

