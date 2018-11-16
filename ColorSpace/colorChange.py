# -*- coding:utf-8 -*-

import cv2

def colorChange():
    src_img = cv2.imread('D:/win10/CVcodes/cv/Data/Images/000.jpg', 1)
    if src_img is not None:
        gray_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
        hsv_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2HSV)
        cv2.imshow('src_image', src_img)
        cv2.waitKey(0)
        cv2.imshow('gray_image', gray_img)
        cv2.waitKey(0)
        cv2.imshow('hsv_image', hsv_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    colorChange()