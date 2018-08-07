from PIL import Image

def wmark(originalphoto,watermark):
    photo=Image.open(originalphoto)
    watermark=Image.open(watermark)
    photo.paste(watermark, (25, 25), watermark)
    photo.save(originalphoto)
