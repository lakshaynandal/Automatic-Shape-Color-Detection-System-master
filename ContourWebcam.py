import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    im_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(frame, 80, 240, 3)

    _, thresh = cv2.threshold(canny, 127, 255, 0)

    # cv2.imshow("Coloured", frame)
    contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # print(contours)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)


    # cv2.imshow("GrayScale", im_gray)
    # cv2.imshow("Frame",frame)

    cv2.imshow("Contours", frame)
    cv2.waitKey(1)

    cv2.imshow("Contours_Canny", frame)
    cv2.imshow('canny', canny)
    cv2.waitKey(1)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
