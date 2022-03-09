#pylint:disable=no-member

import cv2 as cv
# import matplotlib.pyplot as plt

img = cv.imread('/Users/webileapp/Desktop/niharika_files/projects/opencv_course_master/Resources/Photos/park.jpg')

cv.imshow('Park', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)
#
# # BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)
#
# # BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
#
# # HSV to BGR
lab_bgr = cv.cvtColor(img, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)
# blur = cv.GaussianBlur(img, (3,3),  cv.BORDER_DEFAULT)
# cv.imshow("blur", blur)

# cany = cv.Canny(img,125,175)
# # cv.imshow("blur", cany)
#
# dilation = cv.dilate(cany,(7,7),iterations=3)
# # cv.imshow("blur", dilation)
#
# eroded = cv.erode(dilation,(3,3),iterations=1)
# # cv.imshow("blur",eroded)
#
# resize = cv.resize(img, (500, 500))
# cv.imshow("resized", resize)
cv.waitKey(0)