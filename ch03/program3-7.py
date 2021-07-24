import pandas as pd
import matplotlib.pyplot as plt

filePath = "F://BaiduNetdiskDownload//OpenCV+TensorFlow//code//dataTest.csv"
dataFile = pd.read_csv(filePath, header=None, prefix="V")

target = []
for i in range(200):
    if dataFile.iat[i, 10] >= 7:
        target.append(1.0)
    else:
        target.append(0.0)

dataRow = dataFile.iloc[0:200, 10]
plt.scatter(dataRow, target)
plt.xlabel("Attribute")
plt.ylabel("Target")
plt.show()
