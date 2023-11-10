import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(20,100),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255))
cv2.putText(img,"Mercury",(110,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Venus",(190,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.imwrite("solar.jpg",img)