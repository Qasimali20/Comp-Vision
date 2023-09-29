import cv2 as cv

# Read in an image
img = cv.imread('images/Madonna.jpeg')
cv.resize(img, (100,100), interpolation=cv.INTER_CUBIC)
cv.imshow('Madonna', img)
