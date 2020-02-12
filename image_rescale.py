from PIL import Image
import os
import sys

thumbnail_size = 256, 256
os.chdir('output/images')
files = os.walk('.')
# try:
#     os.mkdir('output/images/thumbnails')
# except:
#     pass
for z in files:
    for x in z[2]:
        if ('jpg' in x) or ('jpeg' in x):
            image = Image.open(os.path.join(z[0], x))
            # image.thumbnail(thumbnail_size)
            # image.save('output/images/thumbnails/'+x)
        # elif 'jpeg' in x:
        #     image = Image.open('output/images/'+x)
            # image.save('output/images/thumbnails/'+x)
        else:
            continue
        image.thumbnail(thumbnail_size)
        try:
            os.mkdir(os.path.join('thumbnails',z[0]))
        except:
            pass
        image.save(os.path.join('thumbnails', z[0], x), "jpeg")



