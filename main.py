import cv2
import numpy as np
import glob
# import json
# import pandas
# images_png=glob.glob("/Users/yaakov/downloads/YLM-pic-down/*.png")
# 读取文件夹内要处理的所有的图片
images=glob.glob("/Users/yaakov/downloads/YLM-pic-down/*.*")
# 对文件夹内的图片进行分类
#读取水印文件
wm=cv2.imread("/Users/yaakov/Documents/wm.png")
# cv2.imshow("watermark",wm)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
for image in images:
    # num=0:images_num+1
    img=cv2.imread(image,1)
    shape=img.shape #获取图片的高度和宽度保存到一个数组里面
    # print(type(shape))
    List=list(shape)
    hight=List[0]#获取图片的高度
    width=List[1]#获取图片的宽度
    #第一步对图片进行旋转处理
    if hight < width: #1.把横向的图片旋转90°
        img=np.rot90(img)
        num=uuid.uuid4
        cv2.imwrite(image,img) #将处理好的图片保存到原来的位置替换之前的图片.
    #第二步,统一图片尺寸
    img=cv2.resize(img,(800,1600))
    # cv2.imshow("正在添加水印",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #第三部需要将图片打水印
    #python 竟然可以去掉水印,也就是说可以利用这个功能去掉 shutterstock 下载的图片的水印!!!
    # image[359:359+watermark.shape[0],453:453+watermark.shape[1]]=watermark
    # img=img+watermark
    # waterred=img+watermark
    # 其实我觉得给图片加水印也可以理解为通过OpenCV 叠加两个图片图层
    # 利用的资源:https://blog.csdn.net/zhonghuan1992/article/details/38456767
    # img=cv2.addWeighted(img,0.9,wm,0.1,0.0) # 后来证明,这个方法是行不通的会把图片的清晰度降低掉,这样子是不行的,只能另找明路.
    # img=cv2.merge(img,wm)
    cv2.imwrite(image,img) 




    


