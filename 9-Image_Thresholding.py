import os 
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(os.path.join(".","data","img1.jpg"))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")
plt.show()

# eşikleme

_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY_INV )

plt.figure()
plt.imshow(thresh_img, cmap = "gray")
plt.axis("off")
plt.show()

# Adaptive eşik değeri

thresh_img2 = cv2.adaptiveThreshold(img, 250, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)

# cv2.ADAPTIVE_THRESH_MEAN_C = kullanacağımız yöntem
# blocksize(11) = bakılan komşu küme sayısı
# C sayısı (8) = Ortalama eşik sayısı
plt.figure()
plt.imshow(thresh_img2, cmap = "gray")
plt.axis("off")
plt.show()




















