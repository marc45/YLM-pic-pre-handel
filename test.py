from PIL import Image
import glob

photo = Image.open("/Users/yaakov/downloads/YLM-pic-down/mark.png")
watermark = Image.open("/Users/yaakov/Documents/biryol-trans-capa.png")
photo.paste(watermark, (25, 25), watermark)
photo.show("test")