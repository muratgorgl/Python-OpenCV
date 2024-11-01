import cv2
import os

# içe aktarma
img = cv2.imread(os.path.join(".","data","birds.png"), 0)

# görselleştir
cv2.imshow("ilk resim", img)

k = cv2.waitKey(0) & 0xFF

if k ==27: # esc
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("birds_gray.png",img)
    cv2.destroyAllWindows()