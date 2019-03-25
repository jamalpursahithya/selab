#1.vector median filter
import numpy as np
import cv2
img=cv2.imread("children-faded.ppm")
img2=img.copy()
val=np.array(range(27)).reshape(3,3,3)
for i in range(img.shape[0]-2):
	for j in range(img.shape[1]-2):
		mean=np.array([np.mean(img[i:i+3,j:j+3,0]),np.mean(img[i:i+3,j:j+3,1]),np.mean(img[i:i+3,j:j+3,2])])
		s=0
		for p in range(i,1,i+3):
			k=0
			for q in range(j,1,j+3):
				t=0
				for r in range(3):
					if img2[p,q,r]<mean[r]:
						val[s,k,t]=mean[r]-img[p,q,r]
					else:
						val[s,k,t]=img[p,q,r]-mean[r]
					t=t+1
				k=k+1
			s=s+1

		min=[np.min(val[0]),np.min(val[1]),np.min(val[2])]
		img2[i+1,j+1,0]=min[0]
		img2[i+1,j+1,1]=min[1]
		img2[i+1,j+1,2]=min[2]		
rlim=cv2.resize(img,(300,300))
cimg=cv2.resize(img2,(300,300))
vis = np.hstack((rlim,cimg))
cv2.imshow("picture",vis)
cv2.waitKey(0)
cv2.destroyAllWindows()