#导入cv模块
import cv2 as cv
#检测函数
def face_detect_demo():
    gary=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_detect= cv.CascadeClassifier('D:/haarcascade_files/haarcascade_frontalface_alt2.xml')
    face=face_detect.detectMultiScale(gary,1.01,5,0,(100,100),(400,400))
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow('result',img)
#读取图片
img=cv.imread("face01.jpg")
#检测函数
face_detect_demo()
#等待
while True:
    if ord('q')==cv.waitKey(0):
        break
#释放内存
cv.destroyAllWindows()