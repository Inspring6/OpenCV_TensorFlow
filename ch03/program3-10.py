import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

filePath = "F://BaiduNetdiskDownload//OpenCV+TensorFlow//code//dataTest.csv"
dataFile = pd.read_csv(filePath, header=None, prefix="V")

dataFileNormalized = dataFile.iloc[:, 1:6]
summary = dataFileNormalized.describe()
for i in range(5):
    mean = summary.iloc[1, i]  # 均值
    sd = summary.iloc[2, i]  # 标准差，此处的1，2是由sunmmary中的describe决定的
    # dataFileNormalized.iloc[:, i:(i+1)] = (dataFileNormalized.iloc[:, i:(i+1)] - mean) / sd
    dataFileNormalized.iloc[:, i] = (dataFileNormalized.iloc[:, i] - mean) / sd
array = dataFileNormalized.values
matplotlib.pyplot.boxplot(array)
plt.xlabel("Attribute")
plt.ylabel("Score")
plt.show()
