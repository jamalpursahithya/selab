import numpy as np
import cv2
img=cv2.imread("road.jpg")
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cimg_hsv=img_hsv.copy()
# HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255]
h_c=0
h_bw=50
s_c=180
v_c=50
print(img_hsv.shape)
for i in range(img_hsv.shape[0]):
	for j in range(img_hsv.shape[1]):
		if(img_hsv[i,j,0]<(h_c-h_bw) or img_hsv[i,j,0]>(h_c+h_bw)):
			cimg_hsv[i,j,0]=120
		if(img_hsv[i,j,1]<=s_c):
			cimg_hsv[i,j,1]=0
		if(img_hsv[i,j,2]<=v_c):
			cimg_hsv[i,j,2]=0
crimg=cv2.cvtColor(cimg_hsv,cv2.COLOR_HSV2BGR)
rimg=cv2.resize(img,(300,300))
cimg=cv2.resize(crimg,(300,300))
vis = np.hstack((rimg,cimg))
cv2.imshow("road picture",vis)
cv2.waitKey(0)
cv2.destroyAllWindows()