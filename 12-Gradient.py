import os 
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Görüntü gradyanı, görüntüdeki yoğunluk veya renkteki yönlü bir değişiktir.
# Kenar algılamada kullanılır


# resmi içe aktar

img = cv2.imread(os.path.join(".","data","sudoku.jpg"), 0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Img")


# X gradyan
sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 1, dy = 0, ksize = 5)
plt.figure(), plt.imshow(sobelx, cmap = "gray"), plt.axis("off"), plt.title("Sobel X")

# Y gradyan
sobely = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 0, dy = 1, ksize = 5)
plt.figure(), plt.imshow(sobely, cmap = "gray"), plt.axis("off"), plt.title("Sobel Y")

# Laplacian Gradyan
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_16S)
plt.figure(), plt.imshow(laplacian, cmap = "gray"), plt.axis("off"), plt.title("Laplacian")
