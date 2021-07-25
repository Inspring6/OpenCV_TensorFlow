import numpy as np
import cv2
from scipy import ndimage

img = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(img, (11, 11), cv2.IMREAD_GRAYSCALE)
gaussImg = img - blurred
cv2.imshow("img", img)
cv2.imshow("gaussImg", gaussImg)
cv2.imshow("blurred", blurred)
cv2.waitKey()
