# -*- coding:utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

def filter():
    src_img = cv2.imread('D:/win10/CVcodes/cv/Data/Images/000.jpg', 1)
    gray_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    # 平滑空间滤波
    #   均值滤波
    blur_img = cv2.blur(src_img, (3, 3))
    #   中值滤波
    median_img = cv2.medianBlur(src_img, 3)

    plt.subplot(231)
    plt.imshow(src_img)
    plt.title('Source Image')

    plt.subplot(232)
    plt.imshow(gray_img, 'gray')
    plt.title('Gray Image')

    plt.subplot(233)
    plt.imshow(blur_img)
    plt.title('Blur Image')

    plt.subplot(234)
    plt.imshow(median_img)
    plt.title('MedianBlur Image')

    plt.show()

def sharpen():
    src_img = cv2.imread('D:/win10/CVcodes/cv/Data/ImagesMaterial/DIP3E_Original_Images_CH03/Fig0338(a)(blurry_moon).tif', 0)
    # gray_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    # Laplacian算子锐化
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    edge_img = cv2.filter2D(src_img, -1, kernel)
    outpur_img = cv2.add(src_img, edge_img)

    plt.subplot(131)
    plt.imshow(src_img, 'gray')
    plt.title('Gray Image')

    plt.subplot(132)
    plt.imshow(edge_img, 'gray')
    plt.title('Edge Image')

    plt.subplot(133)
    plt.imshow(outpur_img, 'gray')
    plt.title('Sharpen Image')

    plt.show()

if __name__ == '__main__':
    # filter()
    sharpen()
