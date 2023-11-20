from PIL import Image, ImageEnhance, ImageFilter
import os

#two folders, the first for the original images and the second for the edited images
path = './imgs'
pathOut = '/editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    #makes the image look cleaner
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
    #makes image less pixelated
    edit = img.filter(ImageFilter.SMOOTH_MORE)
    #add contrast to the image
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(1.5)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')