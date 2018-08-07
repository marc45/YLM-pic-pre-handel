import glob
import cv2
import numpy as np
from watermark import *
from resizecrop import *


#读取文件夹内所有需要处理的照片
images=glob.glob("/Users/yaakov/downloads/YLM-pic-down/*.*")
#对照片进行旋转操作
for image in images:
    imgcv2=cv2.imread(image) #读取照片
    #读取照片的宽高等数据
    imgshape=imgcv2.shape
    # print(imgshape)
    #将照片信息转换为数组文件,这样方便索引处理
    shapeList=list(imgshape)
    height=shapeList[0]
    width=shapeList[1]
    if height < width: #1.把横向的图片旋转90°
        imgcv2=np.rot90(imgcv2)
        cv2.imwrite(image,imgcv2) #将图片覆盖写入
    resizecrop(image,image,800,1600)
    watermark="/Users/yaakov/Documents/biryol-trans-capa.png"
    wmark(image,watermark)