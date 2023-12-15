import cv2
import pyautogui
import numpy as np

ss=pyautogui.screenshot()

frame=np.array(ss)
frame=cv2.resize(frame,(1000,1000))
frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
cv2.imshow("RGB",frame)
frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
cv2.imshow("GRAY",frame)
cv2.imwrite("ss_gray.jpg",frame)


cv2.waitKey(0)
cv2.destroyAllWindows()
