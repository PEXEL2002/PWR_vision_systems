import cv2
import numpy as np

image_path = 'rynek_frag.jpg'
angle = -30
maxCorners = 100
qualityLevel = 0.4
minDistance = 10
blockSize = 3

img = cv2.imread(image_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('01_gray.png', gray)

gray = cv2.GaussianBlur(gray, (9, 9), 1.5)
corners_original = cv2.goodFeaturesToTrack(
    image=gray,
    maxCorners=maxCorners,
    qualityLevel=qualityLevel,
    minDistance=minDistance,
    blockSize=blockSize
)
corners_original = corners_original.astype(int)

img_with_corners = img.copy()
for pt in corners_original:
    x, y = pt[0]
    cv2.circle(img_with_corners, (x, y), 4, (0, 0, 255), -1)

cv2.imwrite('02_corners_original.png', img_with_corners)

(h, w) = gray.shape
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(gray, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
cv2.imwrite('03_rotated.png', rotated)

corners_rotated = cv2.goodFeaturesToTrack(
    image=rotated,
    maxCorners=maxCorners,
    qualityLevel=qualityLevel,
    minDistance=minDistance,
    blockSize=blockSize
)
corners_rotated = corners_rotated.astype(int)

rotated_colored = cv2.cvtColor(rotated, cv2.COLOR_GRAY2BGR)
for pt in corners_rotated:
    x, y = pt[0]
    cv2.circle(rotated_colored, (x, y), 4, (0, 255, 0), -1)

cv2.imwrite('04_corners_rotated.png', rotated_colored)

transformed_pts = cv2.transform(np.array([corners_original[:, 0]], dtype=np.float32), M)[0]

for pt in transformed_pts:
    x, y = pt.ravel()
    cv2.circle(rotated_colored, (int(x), int(y)), 3, (255, 0, 0), 1)  # Niebieskie – transformacja

cv2.imwrite('05_comparison.png', rotated_colored)

print(f'Liczba rogów (oryginał): {len(corners_original)}')
print(f'Liczba rogów (po obrocie): {len(corners_rotated)}')
