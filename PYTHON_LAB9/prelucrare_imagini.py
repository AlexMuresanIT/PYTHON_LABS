import numpy as np
import cv2

img=cv2.imread("apple.jpg",1)
dsize=(500,500)
img=cv2.resize(img,dsize)
#cv2.imshow("Mere",img)

img_cvt=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#cv2.imshow("Convertita",img_cvt)

edges=cv2.Canny(img,100,70)
#cv2.imshow("Contur",edges)

template=cv2.imread("template.jpg",0)
frame=cv2.imread("frame.jpg",0)

template=cv2.resize(template,dsize)
frame=cv2.resize(frame,(200,200))

cv2.imshow("Template",template)
cv2.imshow("Frame",frame)

result=cv2.matchTemplate(frame,template,cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
cv2.circle(result,max_loc, 15,255,2)
cv2.imshow("Matching",result)




cv2.waitKey(0)
cv2.destroyAllWindows()
