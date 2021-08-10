import numpy as np
import cv2

# img = np.mat(np.zeros((300, 300), dtype=np.uint8))
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# cv2.imshow("test", img)
# print(img.shape)
# cv2.waitKey()

img = cv2.imread("../jpg/2.jpg", cv2.IMREAD_GRAYSCALE)  # 读取灰度图像
cv2.imwrite("../jpg/2_1.png", img)
cv2.imshow("img", img)
cv2.waitKey()
