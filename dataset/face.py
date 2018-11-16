import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)
ret, vid = cap.read()

while(True):
    if not ret:
        continue



# Converting image to grayscale
gray = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
gray = np.array(gray, dtype='uint8')

# Searching for face cordinates and saving cordinates
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Drawing rectangle in saved cordinates
for (x, y, w, h) in faces:
    cv2.rectangle(vid, (x, y), (x + w, y + h), (125, 255, 0), 2)

# Displaying the Image
cv2.imshow('vid', vid)

# If q is pressed exit program
if cv2.waitKey(1) & 0xFF == ord('q'):
    break