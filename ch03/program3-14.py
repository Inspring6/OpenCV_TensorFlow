from pylab import *
import pandas as pd
import matplotlib.pyplot as plot

filePath = "F://BaiduNetdiskDownload//OpenCV+TensorFlow//code//rain.csv"
dataFile = pd.read_csv(filePath)
summary = dataFile.describe()
minRings = -1
maxRings = 99
nrows = 11

for i in range(nrows):
    dataRow = dataFile.iloc[i,1:13]
    lableColor = (dataFile.iloc[i,12]-minRings)/(maxRings-minRings)
    dataRow.plot(alpha = 0.5)
plot.xlabel("Attribute")
plot.ylabel("Score")
plot.show()