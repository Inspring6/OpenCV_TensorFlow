import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# from pylab import *

filePath = "F://BaiduNetdiskDownload//OpenCV+TensorFlow//code//dataTest.csv"
dataFile = pd.read_csv(filePath, header=None, prefix="V")

print(dataFile.head())
print(dataFile.tail())

summary = dataFile.describe()
print(summary)

array = dataFile.iloc[:,10:16].values
matplotlib.pyplot.boxplot(array)
plt.xlabel("Attribute")
plt.ylabel("Score")
plt.show()