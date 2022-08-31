from distutils.fancy_getopt import fancy_getopt
from inspect import isdatadescriptor
from msilib import PID_LASTAUTHOR
import os
import cv2 as cv
from PIL import Image
import numpy as np

def getImageAndLabels(path):
    #储存人脸数据
    faceSamples=[]
    #储存姓名数据
    ids=[]
    #储存图片信息
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #加载分类器
    face_detect= cv.CascadeClassifier('D:/haarcascade_files/haarcascade_frontalface_default.xml')
    #遍历图表中的图片
    for imagePath in imagePaths:
        #打开图片，灰度变化PIL有九种不同模式：1，L，RGB，RGBA，CMYK，YCbCr，I，F
        PIL_img=Image.open(imagePath).convert('L')
        #将灰度图像转换为数据，以黑白深浅
        img_numpy=np.array(PIL_img,'uint8')
        #获得人脸特征
        faces=face_detect.detectMultiScale(img_numpy)
        #获取每张图片的id和姓名
        id=int(os.path.split(imagePath)[1].split('.')[0])
        #预防无面容图片
        for x,y,w,h in faces:
            ids.append(id)
            faceSamples.append(img_numpy[y:y+h,x:x+w])
    #打印脸部特征和id
    print('id:',id)
    print('fs:',faceSamples)
    return faceSamples,ids

if __name__=="__main__":
    #图片路径
    path='D:/4/pic'
    #获取图片数组和ID标签数组和姓名
    faces,ids=getImageAndLabels(path)
    #加载识别器
    recognizer=cv.face.LBPHFaceRecognizer_create()
    #训练
    recognizer.train(faces,np.array(ids))
    #保存文件
    recognizer.write('D:/4/trainer/trainer.yml')