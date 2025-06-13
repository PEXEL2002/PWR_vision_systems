import cv2
import numpy as np

img = cv2.imread("krasnal.jpg")
cv2.imshow("01_oryginal", img)

patch = img[220:240, 100:120]

avg_b = np.mean(patch[:, :, 0])
avg_g = np.mean(patch[:, :, 1])
avg_r = np.mean(patch[:, :, 2])
avg = (avg_b + avg_g + avg_r) / 3

scale_b = avg / avg_b
scale_g = avg / avg_g
scale_r = avg / avg_r

balanced = img.astype(np.float32)
balanced[:, :, 0] *= scale_b
balanced[:, :, 1] *= scale_g
balanced[:, :, 2] *= scale_r

balanced = np.clip(balanced, 0, 255).astype(np.uint8)

cv2.imshow("02_white_balanced", balanced)
cv2.imwrite("white_balanced.jpg", balanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
