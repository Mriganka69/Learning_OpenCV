import cv2 as cv 

# Reading Images
img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Cat', gray)

# Blur an image
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT )
# cv.imshow('Blur', blur)

# Edge Cascade - outline is only shown
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (200,200), interpolation=cv.INTER_CUBIC )
cv.imshow('Resized', resized)

# Cropping image
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)