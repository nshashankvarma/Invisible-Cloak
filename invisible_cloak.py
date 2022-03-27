import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(10,100)


while True:
    ret, background = cap.read()
    cv2.imshow("Background", background)
    key=cv2.waitKey(1)
    if( key==32):
        break
background = np.flip(background, axis=1)

while True:
    ret, frame = cap.read()
    frame = np.flip(frame, axis=1)
    # cv2.imshow("Frame", frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)

    lower_bound = np.array([11,120,109])
    upper_bound = np.array([32,243,255])

    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    masked_not = cv2.bitwise_not(mask)
    res1 = cv2.bitwise_and(frame, frame, mask=masked_not)
    res2  =cv2.bitwise_and(background, background, mask=mask)
    res3 = cv2.addWeighted(res1, 1, res2, 1, 0)
    # cv2.imshow("maskednot", masked_not)
    # cv2.imshow("res1", res1)
    # cv2.imshow("res2", res2)
    cv2.imshow("res3", res3)
    key=cv2.waitKey(1)
    if( key==27):
        break
cv2.destroyAllWindows()
