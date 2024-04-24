
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.stattools import adfuller

#load the data 
data = pd.read_csv("rainfall.csv")
# print(data)

#preprocess the data
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)

#explore the data
plt.plot(data['rainfall'])
plt.title("rainfall dataset")
plt.xlabel('Date')
plt.ylabel('Rainfall')
plt.show()

#time-series decomposition
stl = STL(data['rainfall'], seasonal= 13)
result = stl.fit()
result.plot()
plt.show()



