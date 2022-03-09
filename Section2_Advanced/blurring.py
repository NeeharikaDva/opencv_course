#pylint:disable=no-member

import cv2 as cv

img = cv.imread('/Users/webileapp/Desktop/niharika_files/projects/opencv_course_master/Resources/Photos/cats.jpg')
# mg = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

average1 = cv.blur(img, (2,2))
cv.imshow('Average 1', average1)
# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)
#
# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)