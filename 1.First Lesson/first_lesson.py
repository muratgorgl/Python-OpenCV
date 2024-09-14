# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 15:20:11 2024

@author: Murat
"""

import cv2 
from matplotlib import pyplot as plt


resim=cv2.imread("kizkulesi.jpg",0)

cv2.namedWindow("resim",cv2.WINDOW_NORMAL)


cv2.imshow("resim",resim)


cv2.imshow("resim penceresi",resim)


plt.imshow(resim,cmap="gray")
plt.show()





k=cv2.waitKey(0)
print(k)

if k==27:
    print("ECS tuşuna basıldı")
    
elif k == ord("q"):
    print("q tuşuna basıldı, resim kayıt edildi")
    cv2.imwrite("Kizkulesigri.jpg",resim)
    
    
    
#cv2.destroyWindow("resim penceresi")
cv2.destroyAllWindows()