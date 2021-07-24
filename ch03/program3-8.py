import pandas as pd
import matplotlib.pyplot as plt
from random import uniform

filePath = "F://BaiduNetdiskDownload//OpenCV+TensorFlow//code//dataTest.csv"
dataFile = pd.read_csv(filePath, header=None, prefix="V")

target = []
for i in range(200):
    if dataFile.iat[i, 10] >= 7:
        target.append(1.0 + uniform(-0.3, 0.3))
    else:
        target.append(0.0 + uniform(-0.3, 0.3))
dataRow = dataFile.iloc[0:200, 10]
plt.scatter(dataRow, target, alpha=0.5, s=100)
plt.xlabel("Attribute")
plt.ylabel("Target")
plt.show()

# random.uniform用于生成给定参数范围内的随机数
