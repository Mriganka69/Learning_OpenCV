import cv2 as cv 

# Reading Images
img = cv.imread('Resources/Photos/cat_large.jpg')

cv.imshow('Cat', img)
cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture(0)

while True :
    isTrue, frame = capture.read()  #it will run each frame of the videos
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'): #to break out of while loop with waitkey and 0xFF==ord('d') means if letter d is pressed break out of the while loop
        break

capture.release()
cv.destroyAllWindows()

