import cv2
import numpy as np

# Load and convert to grayscale
img = cv2.imread('kartka.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('01_gray.jpg', gray)
cv2.imshow('Grayscale', gray)

# Strong blur
blurred = cv2.GaussianBlur(gray, (23, 23), 0)
cv2.imwrite('02_blurred.jpg', blurred)
cv2.imshow('Blurred', blurred)

# Thresholding with Otsu and invert
_, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
thresh = cv2.bitwise_not(thresh)
cv2.imwrite('03_threshold.jpg', thresh)
cv2.imshow('Threshold', thresh)

# Edge detection
edges = cv2.Canny(thresh, 50, 150, apertureSize=3)
cv2.imwrite('04_edges.jpg', edges)
cv2.imshow('Edges (Canny)', edges)

# Hough Line detection
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)
line_img = img.copy()

# Draw lines
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(line_img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imwrite('05_lines.jpg', line_img)
cv2.imshow('Detected Lines', line_img)

# Estimate median angle
angles = []
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
        angles.append(angle)

if angles:
    median_angle = np.median(angles)
else:
    median_angle = 0

# Rotate the image
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, median_angle, 1.0)
rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

cv2.imwrite('06_rotated.jpg', rotated)
cv2.imshow('Rotated', rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
