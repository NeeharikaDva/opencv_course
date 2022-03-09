#pylint:disable=no-member

import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)
#
# # 1. Paint the image a certain colour
# blank[200:250, 250:300] = 0,255,0
# cv.imshow('Green', blank)
# #
# # 2. Draw a Rectangle
# cv.rectangle(blank, (0,0), (blank.shape[0]//2, blank.shape[0]//2), (0,0,255), thickness=-1)
# cv.imshow('Rectangle', blank)
# # #
# # # 3. Draw A circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=-1)
# cv.imshow('Circle', blank)

blank[0:100, 0:100] = 0,255,0
blank[100:200, 0:100] = 0,0,255
blank[200:300, 0:100] = 255,0,0
blank[300:400, 0:100] = 100,100,0
blank[400:500, 0:100] = 150,150,0

blank[0:100, 100:200] = 150,150,0
blank[100:200, 100:200] = 100,100,0
blank[200:300, 100:200] = 0,0,255
blank[300:400, 100:200] = 255,0,0
blank[400:500, 100:200] = 0,0,255
# blank[]
# blank[100:200, 200:300] = 255,0,0
# cv.rectangle(blank, (0,0), (blank.shape[0]//4, blank.shape[0]//4), (255,0,0), thickness=-1)
cv.imshow('Rectangle', blank)
# blank[200:250, 250:300] = 0,255,0
# cv.rectangle(blank, (0,0), (blank.shape[0]//4, blank.shape[0]//4), (255,0,0), thickness=-1)
# cv.imshow('Rectangle', blank)
#
# # 4. Draw a line
# cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
# cv.imshow('Line', blank)
#
# # 5. Write text
# cv.putText(blank, 'Hello, my name is Jason!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
# cv.imshow('Text', blank)

cv.waitKey(0)