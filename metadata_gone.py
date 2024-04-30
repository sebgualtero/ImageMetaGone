from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = './editedImgs'

for filename in os.listdir(path):
    img = Image.open(f'{path}/{filename}')

    data = list(img.getdata())

    stripped_image = Image.new(img.mode, img.size)
    stripped_image.putdata(data)

    stripped_image = stripped_image.filter(ImageFilter.SHARPEN).rotate(270)

    clean_name = os.path.splitext(filename)[0]

    stripped_image.save(f'{pathOut}/{clean_name}_stripped.jpg')

    stripped_image.close()