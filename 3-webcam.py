import cv2

# capture
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width, height)

    
# video kaydet
writer = cv2.VideoWriter("video_kaydi.mp4",cv2.VideoWriter_fourcc(*"DIVX"), 20, (width, height))


# cv2.VideoWriter("DIVX"): Çerçevelere sıkıştırmak için codec kodu
#20: fps, videoların hızı
# (width,height): boyutu 

while True:
    ret, frame = cap.read()
    cv2.imshow("webcam",frame)
    
    # save
    
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
writer.release()
cv2.destroyAllWindows()

 