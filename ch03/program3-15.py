from pylab import *
import pandas as pd
import matplotlib.pyplot as plot

filePath = "F://BaiduNetdiskDownload//OpenCV+TensorFlow//code//rain.csv"
dataFile = pd.read_csv(filePath)
summary = dataFile.describe()
corMat = pd.DataFrame(dataFile.iloc[1:20,1:20].corr())

plot.pcolor(corMat)
plot.show()