# -*- coding:utf-8 -*-
import cv2

def hist_equalize():
    src_img = cv2.imread('D:/win10/CVcodes/cv/Data/Images/000.jpg', 1)
    cv2.imshow('src_image', src_img)
    cv2.waitKey(0)
    gray_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray_imgage', gray_img)
    cv2.waitKey(0)
    equal_img = cv2.equalizeHist(gray_img)
    cv2.imshow('equal_image', equal_img)
    cv2.waitKey(0)
    hsv_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv_imgage', hsv_img)
    cv2.waitKey(0)
    equal_img_v = cv2.equalizeHist(hsv_img[:, :, 2])
    hsv_img[:, :, 2] = equal_img_v
    cv2.imshow('hsit_hsv_imgage', hsv_img)
    cv2.waitKey(0)
    

if __name__ == '__main__':
    hist_equalize()