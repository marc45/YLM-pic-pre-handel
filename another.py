import glob
import cv2

images = [cv2.imread(image) for image in glob.glob("/Users/yaakovazat/downloads/YLM-pic-down/*.*")]
for image in images:
    imgcv2=cv2.imread(image) #读取照片
    #读取照片的宽高等数据
    imgshape=imgcv2.shape