# -*- coding:utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

def filter():
    src_img = cv2.imread('D:/win10/CVcodes/cv/Data/Images/000.jpg', 1)
    gray_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)

    # 图像翻转
    rotation_img = np.ones(gray_img.shape, dtype='uint8') * 255 - gray_img

    # 对数变换
    log_img = (gray_img / 255)
    log_img = np.log10(1 + 10*log_img)
    log_img = log_img * 255

    # 伽马变换
    gama_img = gray_img / 255
    gama_img = np.power(gama_img, 0.6)
    gama_img = gama_img * 255


    plt.subplot(231)
    plt.imshow(gray_img, 'gray')
    plt.title('Gray Image')

    plt.subplot(232)
    plt.imshow(rotation_img, 'gray')
    plt.title('Rotation Image')

    plt.subplot(233)
    plt.imshow(log_img, 'gray')
    plt.title('Log Image')

    plt.subplot(234)
    plt.imshow(gama_img, 'gray')
    plt.title('Gama Image')

    plt.subplot(235)
    plt.imshow(src_img)
    plt.title('Source Image')

    plt.show()



if __name__ == '__main__':
    filter()
