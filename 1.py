import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#在下面的程序中，以灰度加载图像，显示图像，按s保存图像并退出，或者按ESC键直接退出而不保存。
img = cv.imread('01.jpg',0)
cv.imshow('image',img)
'''
k = cv.waitKey(0)
if k == 27:         # 等待ESC退出
    cv.destroyAllWindows()
elif k == ord('s'): # 等待关键字，保存和退出
    cv.imwrite('messigray.png',img)
    cv.destroyAllWindows()
'''

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # 隐藏 x 轴和 y 轴上的刻度值
plt.show()