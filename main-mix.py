from PIL import Image
import glob
import cv2
import numpy as np
from watermark_with_transparency import *



# def watermark_with_transparency(input_image_path,
#                                 output_image_path,
#                                 watermark_image_path,
#                                 position):
#     base_image = Image.open(input_image_path)
#     watermark = Image.open(watermark_image_path)
#     width, height = base_image.size
 
#     transparent = Image.new('RGBA', (width, height), (0,0,0,0))
#     transparent.paste(base_image, (0,0))
#     transparent.paste(watermark, position, mask=watermark)
#     transparent.show()
#     transparent.save(output_image_path)
 
 
# if __name__ == '__main__':
#     img = 'lighthouse.jpg'
#     watermark_with_transparency(img, 'lighthouse_watermarked3.jpg',
#                                 'watermark.png', position=(0,0))

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

# 读取使用的水印文件
# watermark=glob.glob("/Users/yaakov/Documents/Watermark/*.*")
# wm=Image.open("/Users/yaakov/Documents/Watermark/biryol-trans-capa.png")
wm=Image.open("/Users/yaakov/Documents/biryol-trans-capa.png")
copied=wm.copy()
testimg=Image.open("/Users/yaakov/downloads/YLM-pic-down/mark.png")
width, height = testimg.size
transparent = Image.new('RGBA', (width, height), (0,0,0,0))
# transparent.show("transparent")
# transparent.paste(testimg, (0,0))
# transparent.show("transparent")
# transparent.paste(wm,position=(0,0), mask=watermark)
# transparent.show()
for image in images:
    imgpil=Image.open(image)
    watermark_with_transparency(imgpil,image,wm,position=(0,0))
