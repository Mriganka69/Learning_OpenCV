import cv2 as cv 

img = cv.imread('Resources/Photos/cat_large.jpg')

cv.imshow('Cat', img)

#Function to resize image or video by changing the scale
def rescaleFrame(frame, scale=0.75):       #It scales the frame with particular scale value 0.75
    # Works for photos, video and live video
    width = int(frame.shape[1] * scale)    # indicated by 1
    height = int(frame.shape[0] * scale)   # indicated by 0
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Another Method to rescale iamge or video using .set
def changeRes(width,height):
    # Works only for live video
    capture.set(3, width)
    capture.set(4, height)



# Rescaling the image
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

# Rescaling Videos
capture = cv.VideoCapture(0)

while True :
    isTrue, frame = capture.read()  

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video',frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): 
        break

capture.release()
cv.destroyAllWindows()


cv.waitKey(0)