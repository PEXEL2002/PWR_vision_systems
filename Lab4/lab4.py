import cv2
import numpy as np

img = cv2.imread('bocian.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("00_grey.png", gray)
cv2.imshow("Szary", gray)

edges = cv2.Canny(gray, 100, 200)
cv2.imwrite("01_krawedzie_canny.png", edges)
cv2.imshow("Wykrywanie krawędzi", edges)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite("02_progowanie.png", thresh)
cv2.imshow("Progowanie", thresh)

kernel = np.ones((5, 5), np.uint8)
opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
cv2.imwrite("03_otwarcie.png", opened)
cv2.imshow("otwarcie", opened)

closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("04_zamkniecie.png", closed)
cv2.imshow("zamkniecie", closed)

cv2.waitKey(0)
cv2.destroyAllWindows()
