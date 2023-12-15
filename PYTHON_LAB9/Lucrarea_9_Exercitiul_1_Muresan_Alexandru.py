import csv
import cv2
import numpy as np

f=open("coordonate.csv","w")
writer=csv.writer(f)



font = cv2.FONT_HERSHEY_COMPLEX
img2 = cv2.imread('mana2.jpg', cv2.IMREAD_COLOR)

img = cv2.imread('mana2.jpg', cv2.IMREAD_GRAYSCALE)
ret, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(threshold, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)

    n = approx.ravel()
    i = 0
    z=1
    for j in n:
        if (i % 2 == 0):
            x = n[i]
            y = n[i + 1]
            string = str(x) + " " + str(y)
            if (i == 0):
                cv2.putText(img2, "Arrow tip", (x, y),font, 0.5, (255, 0, 0))
                writer.writerow((x,y,z))
            else:
                cv2.putText(img2, string, (x, y),font, 0.5, (0, 255, 0))
                writer.writerow((x, y, z))
        i = i + 1

f.close()
cv2.imshow('image2', img2)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()