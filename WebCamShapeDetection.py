import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    im_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(frame, 80, 240, 3)

    _, thresh = cv2.threshold(canny, 127, 255, 0)
    contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cnt1 = 0
    for cnt in contours:
        cnt1 += 1
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        cv2.drawContours(im_gray, [approx], 0, (0), 5)

        # x = approx.ravel()[0]
        # y = approx.ravel()[1]

        # ------------  Center  -------------------------

        M = cv2.moments(cnt)
        # From moment we can calculte area, centroid etc
        # The center or centroid can be calculated as follows
        if(M['m00'])!=0:
            cX = int(M['m10'] / M['m00'])
            cY = int(M['m01'] / M['m00'])

            cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
            area = cv2.contourArea(cnt)

            # Finding shapes
            if len(approx) == 3:
                cv2.putText(frame, "Triangle", (cX, cY), font, .6, (255, 255, 0), 2)
            elif len(approx) == 4 and area >= 35000.0:
                cv2.putText(frame, "Rectangle", (cX, cY), font, .6, (255, 200, 0), 2)
            elif len(approx) == 5:
                cv2.putText(frame, "Pentagon", (cX, cY), font, .6, (255, 0, 0), 2)
            elif 6 < len(approx) < 11:
                cv2.putText(frame, "Star", (cX, cY), font, .6, (255, 0, 0), 2)
            elif 11 < len(approx) < 15:
                cv2.putText(frame, "Ellipse", (cX, cY), font, .6, (255, 0, 0), 2)
            else:
                if area <= 35000.0:
                    cv2.putText(frame, "Circle", (cX, cY), font, .6, (255, 0, 0), 2)

    cv2.imshow("Count & Shapes detected", frame)
    cv2.waitKey(1)

    cv2.putText(frame, 'Shapes Detected : ' + str(cnt1), (50, 520), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    cv2.imshow("Count & Shapes detected", frame)
    cv2.imshow('canny', canny)
    cv2.waitKey(1)

    # cv2.imshow("GrayScale", im_gray)
    # cv2.imshow("Frame",frame)


    key = cv2.waitKey(1)
    if  key == 27:
        break

cap.release()
cv2.destroyAllWindows()
