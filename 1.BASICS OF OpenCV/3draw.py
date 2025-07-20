import cv2 as cv 
import numpy as np 

# Can draw on Cat image too
# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)

#Creating Blank image
blank = np.zeros((500,500,3), dtype='uint8')   # (height,width,colorchannel) , datatype of image is uint8

# 1. Painting the image a certain color
# blank[:] = 0,255,255
# cv.imshow('yellow', blank)

# say we want to color a certain part of the image
# blank[200:300, 300:400] = 255,0,255
# cv.imshow('pink', blank)

# 2. draw a rectangle
# cv.rectangle(blank, (0,0), (250,250) , (255,0,0) , thickness=cv.FILLED)  # instead of (500,250) we can use (blank.shape[1]//2, blank.shape[0]//2)
# cv.imshow('Rectangle',blank)

# 3. draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)  # -1 will fill up the circle
# cv.imshow('Circle', blank)

# 4. Draw a Line
# cv.line(blank, (10,200), (350,500), (255,255,255), thickness=3 )
# cv.imshow('Line', blank)

# Write Text
cv.putText(blank, 'Maeve i love you', (10,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)