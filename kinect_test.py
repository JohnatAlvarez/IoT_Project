# -- coding: utf-8 --
import numpy as np
import cv2
import time
import freenect
 
# Cargamos el vídeo


def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array


classNames =[]
with open("coco.names", "r") as f:
    classNames = f.read().rstrip('\n').split('\n')


img = get_video()



configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt.txt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while 1:
    img = get_video()
    classIds, confs, bbox = net.detect(img,confThreshold = 0.5)
    print(classIds,bbox)

    if len(classIds) != 0:
	for classId, confidence, box in zip(classIds.flatten(),confs.flatten(),bbox):
	    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
	    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
	     
    cv2.imshow("imagen",img)
    cv2.waitKey(1)
