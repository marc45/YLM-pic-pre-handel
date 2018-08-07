import glob
from PIL import Image # 图片加水印我们使用 'pillow' 这个库
import numpy as np
images=glob.glob("/Users/yaakov/downloads/YLM-pic-down/*.*")
for image in images:
    img=Image.open(image)
    # img.show("something")
    count=0
    imgsize=img.size
    imgwidth=img.width
    imgheight=img.height
    print(imgsize)
    if imgheight < imgwidth:
        count +=count
        img.rotate(90)
    img.save(image)
    img.show("Rotated")

