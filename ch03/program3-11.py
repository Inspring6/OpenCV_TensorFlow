from pylab import *
import pandas as pd
import matplotlib.pyplot as plt

filePath = "F://BaiduNetdiskDownload//OpenCV+TensorFlow//code//dataTest.csv"
dataFile = pd.read_csv(filePath, header=None, prefix="V")

summary = dataFile.describe()
minRings = -1
maxRings = 99
nrows = 10
for i in range(nrows):
    dataRow = dataFile.iloc[i,1:10]
    lableColor = (dataFile.iloc[i,10]-minRings)/(maxRings-minRings)
    # dataRow.plot(color = plot.cm.RdYlBl(lableColor),alpha = 0.5)
    dataRow.plot(alpha=0.5)
plt.xlabel("Attribute")
plt.ylabel("Score")
plt.show()