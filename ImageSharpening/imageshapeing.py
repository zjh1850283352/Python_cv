import cv2 as cv
import matplotlib.pyplot as plt

#读取图像信息
img0 = cv.imread("C:/Users/dell/Desktop/1/Python_cv/ImageSharpening/01.jpg")
img1 = cv.resize(img0, dsize = None, fx = 1, fy = 1)
img2 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
cv.imwrite("C:/Users/dell/Desktop/1/Python_cv/ImageSharpening/02.jpg",img2)   #保存灰度图
h, w = img0.shape[:2]
print(h,w)
cv.namedWindow("W0")
cv.imshow("W0",img1)


#Sobel 算子
img3 = cv.Sobel(img2, cv.CV_64F, 0, 1, ksize=5)
cv.namedWindow("W3")
cv.imshow("W3", img3)

#Laplacian 算子
img4 = cv.Laplacian(img2, cv.CV_64F)
cv.namedWindow("W4")
cv.imshow("W4", img4)

#canny 算子
img5 = cv.Canny(img2, 100, 200)
cv.namedWindow("W5")
cv.imshow("W5", img5)

#Scharr 算子
img6 = cv.Scharr(img2, cv.CV_64F, 0, 1)
cv.namedWindow("W6")
cv.imshow("W6", img6)

cv.waitKey(delay = 0)
