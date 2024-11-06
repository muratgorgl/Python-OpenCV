import cv2
import os


img = cv2.imread(os.path.join(".","data","Lenna.png"))
print("Resim Boyutu", img.shape)
cv2.imshow("img",img)

# resized
img_resized = cv2.resize(img,(800,800))
print("Resized Img Shape: ", img_resized.shape)
cv2.imshow("Img Resized",img_resized)

# kırp
img_cropped = img[:200,:300]
cv2.imshow("kirpilmis resim",img_cropped) # width height --> height, width



cv2.waitKey(0)
cv2.destroyAllWindows()