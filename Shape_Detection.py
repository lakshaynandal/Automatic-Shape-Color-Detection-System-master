import cv2
import numpy as np

img = cv2.imread("shapes.jpg")
cv2.imshow("Count & Shapes detected", img)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Count & Shapes detected", img_gray)
cv2.waitKey(0)

_, threshold = cv2.threshold(img_gray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

font = cv2.FONT_HERSHEY_SIMPLEX
cnt1 = 0
for cnt in contours:
    cnt1 += 1
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    cv2.drawContours(img_gray, [approx], 0, (0), 5)

    x = approx.ravel()[0] #height
    y = approx.ravel()[1] #width

    # ------------  Center  -------------------------
    M = cv2.moments(cnt)
    # From moment we can calculte area, centroid etc
    # The center or centroid can be calculated as follows
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])

    cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)
    area = cv2.contourArea(cnt)

    #Finding shapes
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (cX, cY), font,.6, (255, 255, 0),2)
    elif len(approx) == 4 and area <= 50000.0:
        cv2.putText(img, "Rectangle", (cX, cY), font, .6, (255, 200, 0),2)
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (cX, cY), font, .6, (255, 0, 0),2)
    elif 6 < len(approx) < 11:
        cv2.putText(img, "Star", (cX, cY), font, .6, (255, 0, 0),2)
    elif 11 < len(approx) < 15:
        cv2.putText(img, "Ellipse", (cX, cY), font, .6, (255, 0, 0),2)
    else:
        if area <= 50000.0 :
            cv2.putText(img, "Circle", (cX, cY), font, .6,  (255, 0, 0),2)

cv2.imshow("Count & Shapes detected", img)
cv2.waitKey(0)

cv2.putText(img, 'Shapes Detected : ' + str(cnt1), (50, 520), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

cv2.imshow("Count & Shapes detected", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
