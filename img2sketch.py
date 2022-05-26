#Description : This program converts an image to a pencil sketch

#pip install opencv - python

#Import the library
import cv2

#get the image location and the image file name 
img_location = 'D:\python\PYTHON PROJECTS'
filename = 'Rayara.jpg'

#Read in the image
img = cv2.imread(img_location + filename)

#Convert the image to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Invert the image
inverted_gray_image = 255 - gray_image

#Blur the image by gaussian function
blurred_img = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

#Invert the blurred image
inverted_blurred_img = 255 - blurred_img;

#Create the pencil sketch image
pencil_sketch_IMG = cv2.divide(gray_image, inverted_blurred_img, scale = 256.0)

#show the image
cv2.imshow('Original Image', img)
cv2.imshow('New Image',pencil_sketch_IMG)
cv2.waitKey(0)