import cv2
import os
import numpy as np



# resmi içe aktar
img = cv2.imread(os.path.join(".","data","Lenna.png"))
cv2.imshow("img", img) 

# yatay
hor = np.hstack((img,img))
cv2.imshow("Horizontal", hor)

# dikey
ver =np.vstack((img,img))
cv2.imshow("Dikey",ver)

cv2.waitKey(0)
cv2.destroyAllWindows()