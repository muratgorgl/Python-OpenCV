import cv2
import os
import numpy as np

img = cv2.imread(os.path.join(".","data","kart.png"))
cv2.imshow("img",img)

width = 400
height = 500

pts1= np.float32([[207,0],[0,473],[540,150],[340,616]])
pts2=np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

# nihai dönüştürülmüş resim
imgOutput = cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("Output Resim", imgOutput)

cv2.waitKey(0)
cv2.destroyAllWindows()

