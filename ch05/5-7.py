import numpy as np
import cv2
from scipy import ndimage

kernel33 = np.array([[-1, -1, -1],
                     [-1, 8, -1],
                     [-1, -1, -1]])

kernel33_D = np.array([[1, 1, 1],
                       [1, -8, 1],
                       [1, 1, 1]])

img = cv2.imread("../jpg/lena.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("img", img)
linghtImg = ndimage.convolve(img, kernel33_D)
cv2.imshow("linghtImg", linghtImg)
darkImg = ndimage.convolve(img, kernel33)
cv2.imshow("darkImg", darkImg)
cv2.waitKey()
