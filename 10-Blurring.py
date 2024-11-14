import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")


# blurring (detayı azaltır, gürültü engeller)
img = cv2.imread(os.path.join(".","data","NYC.jpg"))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("Orijinal"), plt.show()

"""
Ortalama Bulanıklaştırma Yöntemi
"""

dist2 = cv2.blur(img, ksize = (3,3))
plt.figure(), plt.imshow(dist2), plt.axis("off"), plt.title("Ortalama Blur"), plt.show()

"""
Gaussian Blur
"""

gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("Gaussian Blur"), plt.show()

"""
Median Blur
"""

mb = cv2.medianBlur(img, ksize = 3)
plt.figure(), plt.imshow(mb), plt.axis("off"), plt.title("Median Blur"), plt.show()


def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    
    gauss = np.random.normal(mean, sigma, (row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    
    return noisy

# içe aktar normalize et

img = cv2.imread(os.path.join(".","data","NYC.jpg"))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("Orijinal"), plt.show()

gaussianNoisyImage = gaussianNoise(img)
plt.figure(), plt.imshow(gaussianNoisyImage), plt.axis("off"), plt.title("gaussianNoisyImage"), plt.show()


#gauss blur
gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb2), plt.axis("off"), plt.title("with Gaussian Blur"), plt.show()

def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy = np.copy(image)

    # Salt (beyaz) gürültü
    num_salt = int(np.ceil(amount * image.size * s_vs_p))
    coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy[coords[0], coords[1], :] = 1

    # Pepper (siyah) gürültü
    num_pepper = int(np.ceil(amount * image.size * (1 - s_vs_p)))
    coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy[coords[0], coords[1], :] = 0

    return noisy

sp= saltPepperNoise(img)    
plt.figure(), plt.imshow(sp), plt.axis("off"), plt.title("Salt Pepper Noise"), plt.show()   

mb2 = cv2.medianBlur(sp.astype(np.float32), ksize = 3)
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("Median Blur Salt Pepper Noise"), plt.show()   

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    























