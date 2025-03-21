import cv2
import numpy as np
def createMatrix(size):
    matrix = np.zeros((size*2+1, size*2+1))
    print(f"Rozmiar twojej macierzy {matrix.shape}")
    for i in range(size*2+1):
        for j in range(size*2+1):
            print(f"Podaj wartość dla [{i}, {j}]: ", end="")
            matrix[i][j] = int(input())
    print("Twoja macierz wygląda następująco:")
    print(matrix)
    return matrix


while True:
    try:
        size = int(input("Podaj rozmiar macierzy: "))
        if size < 0:
            raise ValueError
        break
    except:
        print("Podaj liczbę naturalną")

def imageInput():
    nameFile = input("Podaj nazwę pliku (*.jpg, *.png): ")
    img = cv2.imread(nameFile)
    return img

def convolve_rgb(image, kernel):
    return np.dstack([
        cv2.filter2D(image[:, :, channel], ddepth=-1, kernel=kernel)
        for channel in range(3)
    ])

img = imageInput()
kernel = createMatrix(size)
cv2.imshow('Mariusz Orginal', img)
cv2.imshow('Mariusz after convolution', convolve_rgb(img,kernel))
cv2.imwrite('mariusz_convolution.jpg', convolve_rgb(img,kernel))
cv2.waitKey(0)
cv2.destroyAllWindows()