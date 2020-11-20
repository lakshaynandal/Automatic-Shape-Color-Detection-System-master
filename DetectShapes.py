import cv2
import numpy as np

img = cv2.imread("shapes1.jpg", cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread("shapes1.jpg")
cv2.imshow("Origional Shapes", img1)
cv2.waitKey(0)

cv2.imshow("Origional Shapes", img)
cv2.waitKey(0)
# img = cv2.resize(img, (500,500))
_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# font = cv2.FONT_HERSHEY_COMPLEX
font = cv2.FONT_HERSHEY_SIMPLEX

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    area = cv2.contourArea(cnt)
    # print(area)
    if len(approx) == 3:
        cv2.putText(img1, "Triangle", (x, y), font,.6, 3)
    elif len(approx) == 4 and area <50000.0:
        cv2.putText(img1, "Rectangle", (x, y), font, .6, 3)
        print(area)
    elif len(approx) == 5:
        cv2.putText(img1, "Pentagon", (x, y), font, .6, 2)
    elif 6 < len(approx) < 11:
        cv2.putText(img1, "Star", (x, y), font, .6, 2)
    elif 11 < len(approx) < 15:
        cv2.putText(img1, "Ellipse", (x, y), font, .6, 2)
    else:
        cv2.putText(img1, "Circle", (x, y), font, .6, 2)
# cv2.imshow("Threshold", threshold)
# cv2.waitKey(0)
cv2.imshow("Shapes", img1)
cv2.waitKey(0)

cv2.destroyAllWindows()
