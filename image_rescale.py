from PIL import Image
import os
import sys

thumbnail_size = 256, 256
files = os.listdir('output/images')
try:
    os.mkdir('output/images/thumbnails')
except:
    pass

for x in files:
    if 'jpg' in x:
        image = Image.open('output/images/'+x)
        # image.thumbnail(thumbnail_size)
        # image.save('output/images/thumbnails/'+x)
    elif 'jpeg' in x:
        image = Image.open('output/images/'+x)
        # image.save('output/images/thumbnails/'+x)
    else:
        continue
    image.thumbnail(thumbnail_size)
    image.save('output/images/thumbnails/'+x, "jpeg")



