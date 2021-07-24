import pandas as pd
import matplotlib.pyplot as plt

filePath = "F://BaiduNetdiskDownload//OpenCV+TensorFlow//code//dataTest.csv"
dataFile = pd.read_csv(filePath, header=None, prefix="V")

dataRow1 = dataFile.iloc[100, 1:300]
dataRow2 = dataFile.iloc[101, 1:300]
plt.scatter(dataRow1, dataRow2)
plt.xlabel("Attribute1")
plt.ylabel("Attribute2")
plt.show()
