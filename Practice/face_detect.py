#pylint:disable=no-member

import cv2 as cv

img = cv.imread('../images/Group2.jpeg')
#cv.imshow('Group of people', img)

haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

faces_rect = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)



cv.waitKey(0)
cv.destroyAllWindows()