import cv2
#import mediapipe
#import time

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    cv2.imshow("image", img)
    cv2.waitKey(1)
cv2.destroyAllWindown()