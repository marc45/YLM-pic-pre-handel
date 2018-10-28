import cv2 as cv
import glob
import numpy as np
from watermark import *
from resizecrop import *

# 读取文件夹内的图片文件
pngs=glob.glob('/Users/yaakovazat/Pictures/YLM-pic-down/*png')
PNGs=glob.glob('/Users/yaakovazat/Pictures/YLM-pic-down/*PNG')
jpgs=glob.glob('/Users/yaakovazat/Pictures/YLM-pic-down/*jpg')
JPGs=glob.glob('/Users/yaakovazat/Pictures/YLM-pic-down/*JPG')
jpegs=glob.glob('/Users/yaakovazat/Pictures/YLM-pic-down/*jpeg')
JPEGs=glob.glob('/Users/yaakovazat/Pictures/YLM-pic-down/*JPEG')

#活的所有图片文件的绝对地址
images=pngs+PNGs+jpegs+jpgs+JPEGs+JPGs
# print(images)
# 对图片进行循环处理:
for image in images:
    img=cv.imread(image)
    imgshape=img.shape
    shapeList=list(imgshape)
    shapeList=list(imgshape)
    height=shapeList[0]
    width=shapeList[1]
    if height < width: #1.把横向的图片旋转90°
        img=np.rot90(img)
        cv.imwrite(image,img) #将图片覆盖写入
    resizecrop(image,image,800,1600)
    watermark="wm.png"
    wmark(image,watermark)
