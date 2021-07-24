import pandas as pd
import matplotlib.pyplot as plt

rocksVMines = pd.DataFrame([[1, 200, 105, 3, False],
                            [2, 165, 80, 2, False],
                            [3, 184.5, 120, 2, False],
                            [4, 116, 70.8, 1, False],
                            [5, 270, 150, 4, True]])

dataRow1 = rocksVMines.iloc[1,0:3]
dataRow2 = rocksVMines.iloc[2,0:3]
plt.scatter(dataRow1,dataRow2)
plt.xlabel("Attribute1")
plt.ylabel("Attribute2")
plt.show()

dataRow3 = rocksVMines.iloc[3,0:3]
plt.scatter(dataRow2,dataRow3)
plt.xlabel("Attribute2")
plt.ylabel("Attribute3")
plt.show()
