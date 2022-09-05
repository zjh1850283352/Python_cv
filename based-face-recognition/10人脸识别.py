import cv2
import numpy as np
import os
# coding=utf-8
import urllib
import urllib.request
import hashlib

#加载训练数据集文件
recogizer=cv2.face.LBPHFaceRecognizer_create()
#加载数据
recogizer.read('D:/Python_cv/based-face-recognition/trainer/jiahua.yml')
#名称
names=[]
#警报全局变量
warningtime=0
#md5加密
def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()
#短信反馈
statusStr = {
    '0': '短信发送成功',
    '-1': '参数不全',
    '-2': '服务器空间不支持,请确认支持curl或者fsocket,联系您的空间商解决或者更换空间',
    '30': '密码错误',
    '40': '账号不存在',
    '41': '余额不足',
    '42': '账户已过期',
    '43': 'IP地址限制',
    '50': '内容含有敏感词'
}
#报警模块
def warning():
    smsapi="http://api.smsbao.com"
    #短信平台账号
    user='18355535960'
    #短信平台密码
    password=md5('123456')
    #要发送的短信内容
    content='【报警】\n原因:xxx\n地点:xxx\n时间:xxx'
    #要发送短信的手机号码
    phone = '15551052315'
    
    data = urllib.parse.urlencode({'u': user, 'p': password, 'm': phone, 'c': content})
    send_url = smsapi + 'sms?' + data
    response = urllib.request.urlopen(send_url)
    the_page = response.read().decode('utf-8')
    print(statusStr[the_page])


#准备识别的图片
def face_detect_demo(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转换为灰度
    face_detector=cv2.CascadeClassifier('D:/haarcascade_files/haarcascade_frontalface_default.xml')
    #face=face_detector.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(300,300))
    face=face_detector.detectMultiScale(gray)
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        #cv2.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,255,0),thickness=1)
        # 人脸识别
        ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        #print('标签id:',ids,'置信评分：', confidence)
        '''if confidence > 80:
            global warningtime
            warningtime += 1
            if warningtime > 100:
               warning()
               warningtime = 0
            cv2.putText(img, 'unkonw', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
        else:
            cv2.putText(img,str(names[ids-1]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)'''
    cv2.imshow('result',img)
    #print('bug:',ids)

def name():
    path = 'D:/Python_cv/based-face-recognition/pic'
    #names = []
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    for imagePath in imagePaths:
       name = str(os.path.split(imagePath)[1].split('.',2)[1])
       names.append(name)


cap=cv2.VideoCapture(0)
name()
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    face_detect_demo(frame)
    if cv2.waitKey(1) == ord('q'):
        break

'''name()
while True:
    flag,frame=cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord(' ') == cv2.waitKey(10):
        break'''
cv2.destroyAllWindows()
cap.release()
#print(names)