import cv2

img=cv2.imread("travis1.jpg",1)
img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
cv2.imshow("Original",img)

img2=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Gray",img2)

img3=cv2.Canny(img,100,100)
cv2.imshow("Contour",img3)

(thresh,img4)=cv2.threshold(img2,30,255,cv2.THRESH_BINARY)
cv2.imshow("blackandwhite",img4)



cv2.waitKey(0)
cv2.destroyAllWindows()