import cv2 

# Load some pre-trained data on face frontals from opencv (haar cascasde algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.html')

# Choose an image to detect faces in 
img = cv2.imread('RDJ.png')

print("Code Complete")