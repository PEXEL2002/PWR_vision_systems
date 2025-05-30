import cv2
import numpy as np
import matplotlib.pyplot as plt

# === 1. Wczytanie obrazu ===
img = cv2.imread('input.jpg')
if img is None:
    raise FileNotFoundError("Nie znaleziono obrazu wejściowego!")

# === 2. Konwersja do skali szarości ===
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Obraz w skali szarości", gray)
cv2.imwrite("01_gray.jpg", gray)

# === 3. Histogram przed wyrównaniem ===
hist_before = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Histogram przed wyrównaniem")
plt.xlabel("Wartość piksela")
plt.ylabel("Liczba pikseli")
plt.plot(hist_before, color='black')
plt.xlim([0, 256])
plt.savefig("02_histogram_before.png")
plt.close()

# === 4. Wyrównanie histogramu ===
equalized = cv2.equalizeHist(gray)
cv2.imshow("Obraz po wyrównaniu histogramu", equalized)
cv2.imwrite("03_equalized.jpg", equalized)

# === 5. Histogram po wyrównaniu ===
hist_after = cv2.calcHist([equalized], [0], None, [256], [0, 256])
plt.figure()
plt.title("Histogram po wyrównaniu")
plt.xlabel("Wartość piksela")
plt.ylabel("Liczba pikseli")
plt.plot(hist_after, color='black')
plt.xlim([0, 256])
plt.savefig("04_histogram_after.png")
plt.close()

cv2.waitKey(0)
cv2.destroyAllWindows()
