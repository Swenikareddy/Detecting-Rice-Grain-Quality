import cv2
import numpy as np
from matplotlib import pyplot as plt


def get_classificaton(ratio):
	ratio =round(ratio,1)
	toret=""
	if(ratio>=3):
		toret="The average ratio of given sample of grains is "+str(ratio)+".This type of rice is considered as slender long-grain rice and of very good quality.The grains are seperate,light,fluffy once cooked and it is also good for health."
	elif(ratio>=2.1 and ratio<3):
		toret="The average ratio of given sample of grains is "+str(ratio)+".This type of rice is considered as medium size.The rice when cooked remains moist and tender with a moderate stikiness.This can be considered as medium quality of rice."
	elif(ratio>=1.1 and ratio<2.1):
		toret="The average ratio of given sample of grains is "+str(ratio)+".This type of rice is considered as bold. This type of rice has a considerable amount of starch content which may not be suitable for all.The grains become sticky once cooked."
	elif(ratio<=1):
		toret="The average ratio of given sample of grains is "+str(ratio)+".This type of rice is considered as round.This type of rice has high starch content.Starches are linked to a higher risk of diabetes and weight gain and it is not suitable for all bodies."
	#toret="("+toret+")"
	return toret
#rnjn
def ratio():
	l=[]
	print("Starting")
	img = cv2.imread('E:/ricegrain/buttonpython/media/temp.png',0)#load in greyscale mode
	#convert into binary
	ret,binary = cv2.threshold(img,160,255,cv2.THRESH_BINARY)# 160 - threshold, 255 - value to assign, THRESH_BINARY_INV - Inverse binary

	#averaging filter
	kernel = np.ones((5,5),np.float32)/9
	dst = cv2.filter2D(binary,-1,kernel)# -1 : depth of the destination image


	kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

	#erosion
	erosion = cv2.erode(dst,kernel2,iterations = 1)

	#dilation 
	dilation = cv2.dilate(erosion,kernel2,iterations = 1)

	#edge detection
	edges = cv2.Canny(dilation,100,200)

	### Size detection
	contours,hierarchy = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	print ("No. of rice grains=",len(contours))
	total_ar=0
	for cnt in contours:
		x,y,w,h = cv2.boundingRect(cnt)
		aspect_ratio = float(w)/h
		if(aspect_ratio<1):
			aspect_ratio=1/aspect_ratio
		print (round(aspect_ratio,2))
		total_ar+=aspect_ratio
	avg_ar=total_ar/len(contours)
	#print ("Average Aspect Ratio=",round(avg_ar,2),get_classificaton(avg_ar))
	#l=[round(avg_ar,2),get_classificaton(avg_ar)]
	return(get_classificaton(avg_ar))
