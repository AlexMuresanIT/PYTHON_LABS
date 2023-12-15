import cv2

webcam=cv2.VideoCapture(0)

while True:
    ret,cadru=webcam.read()
    gri = cv2.cvtColor(cadru, cv2.COLOR_RGB2GRAY)
    color=cv2.Canny(cadru,100,70)
    cv2.imshow("Normal",cadru)
    cv2.imshow("Gray",gri)
    cv2.imshow("Color", color)
    cv2.imwrite("webcam_photo.jpg",cadru)
    cv2.imwrite("cannt.jpg",color)
    if cv2.waitKey(1)& 0xFF==ord("1"):
        break

webcam.release()
cv2.destroyAllWindows()