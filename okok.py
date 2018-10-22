import glob
import cv2
import numpy as np
from watermark import *
from resizecrop import *
from PIL import Image

images=[]
for image in glob.glob("/Users/yaakovazat/downloads/YLM-pic-down/*.*"):
    imgcv2=cv2.imread(image)
    imgshape=imgcv2.shape
    shapeList=list(imgshape)
