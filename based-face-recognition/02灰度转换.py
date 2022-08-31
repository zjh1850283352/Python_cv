#导入cv模块
import cv2 as cv
#读取图片
img=cv.imread("face01.jpg")
#灰度转换
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#灰度显示
cv.imshow('gray',gray_img)
#储存灰度图片
cv.imwrite('gray_face01.jpg',gray_img)
#显示图片
cv.imshow("read_img",img)
#等待
cv.waitKey(0)
#释放内存
cv.destroyAllWindows()