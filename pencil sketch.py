import cv2
import numpy as np

#reading imagae from file
img = cv2.imread("cat.png")#add you png or jpg file here.
kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1, 9,-1],
                              [-1,-1,-1]])
sharpened = cv2.filter2D(img,-1,kernel_sharpening)
gray = cv2.cvtColor(sharpened , cv2.COLOR_BGR2GRAY)
inv = 255-gray
gaussgray = cv2.GaussianBlur(inv,ksize=(15,15),sigmaX=0,sigmaY=0)
#PENCIL SKETCH EFFECT
def dodgeV2(image,mask):
    return cv2.divide(image,255-mask,scale=256)
pencil_img = dodgeV2(gray,gaussgray)
print('Pencil Sketch effect Applied.')

#comparing original vs resized
cv2.imshow('ORIGINAL',img)
cv2.imshow('PENCIL-SKETCH',pencil_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
