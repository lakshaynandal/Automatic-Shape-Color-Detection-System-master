import cv2
import numpy as np

img = cv2.imread("shapes3D.jpg", cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread("shapes3D.jpg")

cv2.imshow("Count & Shapes detected", img1)
cv2.waitKey(0)
cv2.imshow("Count & Shapes detected", img)
cv2.waitKey(0)

# img = cv2.resize(img, (500,500))
_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# font = cv2.FONT_HERSHEY_SIMPLEX
cnt1 =0
for cnt in contours:
    cnt1 +=1
    cv2.drawContours(img1, [cnt], -1, (0, 255, 0), 2)
cv2.imshow('Count & Shapes detected', img1)
cv2.waitKey(0)

cv2.putText(img1, 'Shapes Detected : ' + str(cnt1-1), (50, 425), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv2.imshow("Count & Shapes detected", img1)
cv2.waitKey(0)

cv2.destroyAllWindows()
