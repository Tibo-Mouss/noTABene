
import sys
from math import floor
import numpy as np
import argparse
import PIL
from PIL import Image
import cv2

def extractImages(pathIn, pathOut):
    count = 0
    
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    x = floor(image.shape[0]/10)
    y = floor(image.shape[1]/10)
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*250))    # added this line 
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        if success:
            image = findTeacher(image)
            cv2.imwrite( pathOut + "/frame%d.jpg" % count, image)     # save frame as JPEG file
            count = count + 1
    nb_frames = count
    images = np.zeros((nb_frames,x*10,y*10,3 ))
    for i in range(0,10):
        images[i] = cv2.imread("./frame"+str(i)+".jpg")
    imageFinale = np.zeros(images[0].shape)
    for i in range(x):
        for j in range(y):
            
            for i_sub in range(10):
                for j_sub in range(10):
                    count0 = 0
                    val0 = 0
                    count1 = 0
                    val1 = 0
                    count2 = 0
                    val2 = 0
                    for im in range(nb_frames):
                        pix = images[im][i*10+i_sub][j*10+j_sub][0]
                        if pix != 0:
                            count0+=1
                        val0 += pix
                        pix = images[im][i*10+i_sub][j*10+j_sub][1]
                        if pix != 0:
                            count1+=1
                        val1 += pix
                        pix = images[im][i*10+i_sub][j*10+j_sub][2]
                        if pix != 0:
                            count2+=1
                        val2 += pix
                    imageFinale[i*10+i_sub][j*10+j_sub][0] = 0 if count0 == 0 else np.uint8(floor(val0/count0))
                    imageFinale[i*10+i_sub][j*10+j_sub][1] = 0 if count1 == 0 else np.uint8(floor(val1/count1))
                    imageFinale[i*10+i_sub][j*10+j_sub][2] = 0 if count2 == 0 else np.uint8(floor(val2/count2))
    cv2.imwrite( args.pathOut + "/final.jpg", imageFinale)
        
        

def findTeacher(image):
    x = floor(image.shape[0]/10)
    y = floor(image.shape[1]/10)
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for i in range(x):
        for j in range(y):
            mean = 0
            for i_sub in range(10):
                for j_sub in range(10):
                    a = (int(grey[i*10+i_sub][j*10+j_sub]))/100
                    mean += a
            if mean<165:
                for i_sub in range(10):
                    for j_sub in range(10):
                        image[i*10+i_sub][j*10+j_sub][0] = np.uint8(0)
                        image[i*10+i_sub][j*10+j_sub][1] = np.uint8(0)
                        image[i*10+i_sub][j*10+j_sub][2] = np.uint8(0)
    return image
                    


if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    extractImages(args.pathIn, args.pathOut)
    
