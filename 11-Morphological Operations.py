import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Morfolojik Operasyonlar
# Erozyon, Genişleme, Açma, Kapatma ve morfolojik gradyan gibi morfolojik operasyonların ne olduklarını öğreneceğiz



# resmi içe aktar
img = cv2.imread(os.path.join(".","data","datai_team.jpg"),0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Orijinal Img") 

# erozyon
# Erozyonun temel fikri sadece toprak erozyonu gibidir, ön plandaki nesnenin sınırlarını aşındırır.
kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("Erozyon") 

# genişleme dilation
# Erozyonun tam tersidir. Görüntüdeki beyaz bölgeyi artırır.
result2 = cv2.dilate(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("Dilation") 

# white noise
whiteNoise = np.random.randint(0, 2, size = img.shape[:2])
whiteNoise = whiteNoise * 255
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("noise_img") 

noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap = "gray"), plt.axis("off"), plt.title("Img w whiteNoise") 

# açılma
# Açılma, erozyonun + genişlemesidir. Gürültünün giderilmesinde faydalıdır.
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("Açılma") 

# kapatma
blackNoise = np.random.randint(0, 2, size = img.shape[:2])
blackNoise = blackNoise * -255
plt.figure(), plt.imshow(blackNoise, cmap = "gray"), plt.axis("off"), plt.title("Black Noise") 

black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off"), plt.title("Black Noise Img") 

# kapatma 
# Kapanış, açmanın tam tersidir
# Genişleme + erozyon
# Ön plandaki nesnelerin içindeki küçük delikleri veya nesne üzerindeki kküçük siyah noktaları kapatmak için kullanışlıdır.
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("Kapama") 

# gradient
# Morfolojik gradyan, bir görüntünün genişlemesi ve erozyonu arasındak farktır.
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap = "gray"), plt.axis("off"), plt.title("Gradyan") 
















