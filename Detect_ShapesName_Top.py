import cv2
import numpy as np

img = cv2.imread("shapes.jpg", cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread("shapes.jpg")
cv2.imshow("Shapes Detected and Count Images", img1)
cv2.waitKey(0)
# img = cv2.resize(img, (500,500))
_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# font = cv2.FONT_HERSHEY_COMPLEX
font = cv2.FONT_HERSHEY_SIMPLEX
cnt1 =0
for cnt in contours:
    cnt1 +=1
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    #------------  Center  -------------------------
    M = cv2.moments(cnt)
    # From moment we can calculte area, centroid etc
    # The center or centroid can be calculated as follows
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])
    #---------------- end  --------------------------
    # print(x,y)
    cv2.drawContours(img1, [cnt], -1, (0, 255, 0), 2)
    if len(approx) == 3:
        cv2.putText(img1, "Triangle", (x, y), font,.6, (255, 0, 0),2)
    elif len(approx) == 4:
        cv2.putText(img1, "Rectangle", (x, y-5), font, .6, (255, 0, 0),2)
    elif len(approx) == 5:
        cv2.putText(img1, "Pentagon", (x, y-5), font, .6, (255, 0, 0),2)
    elif 6 < len(approx) < 11:
        cv2.putText(img1, "Satr", (x, y-5), font, .6, (255, 0, 0),2)
    elif 11 < len(approx) < 15:
        cv2.putText(img1, "Ellipse", (x, y-5), font, .6, (255, 0, 0),2)
    else:
        cv2.putText(img1, "Circle", (x, y-5), font, .6,  (255, 0, 0),2)

# print(cnt1-1)

# cv2.imshow("Threshold", threshold)
# cv2.waitKey(0)
# cv2.imshow("Shapes", img1)
# cv2.waitKey(0)
cv2.putText(img1, 'Shapes Detected : ' + str(cnt1), (50, 380), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow("Shapes Detected and Count Images", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
