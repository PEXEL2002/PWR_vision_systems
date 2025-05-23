import cv2
import numpy as np
image = cv2.imread('foto.jpg')
if image is None:
    raise FileNotFoundError("Nie znaleziono pliku obrazu!")

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 70, 50])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imwrite('wynik_maska.jpg', mask)
cv2.imwrite('wynik_kwiat.jpg', result)
cv2.imwrite('hsv_image.jpg', hsv_image)