# -- coding: utf-8 --
import numpy as np
import cv2
import time
import freenect
import math
# Cargamos el vídeo

KNOWN_DISTANCE = 76.2  # centimeter
# width of face in the real world or Object Plane
KNOWN_WIDTH = 14.3  # centimeter


def get_video():
	array,_ = freenect.sync_get_video()
	array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
	return array
def get_depth():
    	array,_ = freenect.sync_get_depth()
   	array = array.astype(np.uint8)
    	return array

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def focal_length(measured_distance, real_width, width_in_rf_image):

	focal_length_value = (width_in_rf_image * measured_distance) / real_width
	return focal_length_value


def distance_finder(focal_length, real_face_width, face_width_in_frame):
	distance = (real_face_width * focal_length) / face_width_in_frame
	return distance
	
	
guia=get_video()
cv2.imwrite('frame'+'.png',guia)

def face_data(image):
   

	face_width = 0
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray_image, 1.3, 5)
	for (x, y, h, w) in faces:
        	cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0),2)
        	face_width = w

	return face_width

ref_image = cv2.imread("frame.png")

ref_image_face_width = face_data(ref_image)
focal_length_found = focal_length(KNOWN_DISTANCE, KNOWN_WIDTH, ref_image_face_width)
print(focal_length_found)
cv2.imshow("ref_image", ref_image)

while 1:
	img = get_video()
	face_width_in_frame = face_data(img)
	
	if face_width_in_frame != 0:
		Distance = distance_finder(focal_length_found, KNOWN_WIDTH, face_width_in_frame)
		print({round(Distance,2)})
	cv2.imshow("frame", img)
    	k = cv2.waitKey(30)
    	
   	if k == 27:
		break
cap.release()
