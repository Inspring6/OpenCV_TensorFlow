import numpy as np
import cv2

image = np.mat(np.zeros((300, 300), dtype=np.uint8))
imageByteArray = bytearray(image)
print(imageByteArray)
imageRGB = np.array(imageByteArray).reshape(300, 300)
cv2.imshow("cool", imageRGB)
cv2.waitKey()
