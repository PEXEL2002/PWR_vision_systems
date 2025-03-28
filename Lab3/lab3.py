import cv2
import numpy as np
def process_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cropped = gray[68:580, 100:750]
    return cropped
def simple_thresholding(img):
    _, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return thresh1
def adaptive_thresholding(img):
    adaptive_thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)
    adaptive_thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)
    return adaptive_thresh1, adaptive_thresh2
def otsu_thresholding(img):
    _, otsu_thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    return otsu_thresh

img = cv2.imread('termo.jpg')
cv2.imshow('Original image', img)
cropped = process_image(img)
cv2.imshow('Cropped image', cropped)
cv2.imwrite('Cropped_image.jpg', cropped)

thresh = simple_thresholding(cropped)
cv2.imshow('Simple Thresholding', thresh)
cv2.imwrite('Simple_Thresholding.jpg', thresh)

adaptive_thresh1, adaptive_thresh2 = adaptive_thresholding(cropped)
cv2.imshow('Adaptive Thresholding Mean', adaptive_thresh1)
cv2.imwrite('Adaptive_Thresholding_Mean.jpg', adaptive_thresh1)
cv2.imshow('Adaptive Thresholding Gaussian', adaptive_thresh2)
cv2.imwrite('Adaptive_Thresholding_Gaussian.jpg', adaptive_thresh2)

otsu_thresh = otsu_thresholding(cropped)
cv2.imshow('Otsu Thresholding', otsu_thresh)
cv2.imwrite('Otsu_Thresholding.jpg', otsu_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
