import cv2
img = cv2.imread('face-of-male-mandrill-baboon-mandrillus-animal-images.jpg')
cv2.rectangle(img, (100, 100), (500, 250), (0, 255, 0), 2)

cv2.circle(img, (300, 60), 40, (0, 0, 255), 2)

cv2.ellipse(img, (320, 360), (80, 40), 90, 0, 360, (0, 255, 255), 2)

cv2.imshow('Mariusz', img)
cv2.imwrite('mariusz.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
