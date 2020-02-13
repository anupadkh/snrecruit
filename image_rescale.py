from PIL import Image
import os
import sys

thumbnail_size = 256,256
folder_location = os.path.dirname(__file__)
os.chdir(os.path.join(folder_location,'output', 'images'))
files = os.walk('.')
try:
    os.mkdir('thumbnails')
except:
    pass
for z in files:
    try:
        cwd_path = z[0].split('./')[1]
    except:
        cwd_path = z[0]
    if cwd_path == '.':
        cwd_path = ''
    if 'thumbnails' in cwd_path:
        continue
    for x in z[2]:
        if ('jpg' in x) or ('jpeg' in x):
            image = Image.open(os.path.join(cwd_path, x))
            # image.thumbnail(thumbnail_size)
            # image.save('output/images/thumbnails/'+x)
        # elif 'jpeg' in x:
        #     image = Image.open('output/images/'+x)
            # image.save('output/images/thumbnails/'+x)
        else:
            continue
        image.thumbnail(thumbnail_size)
        try:
            os.mkdir(os.path.join('thumbnails', cwd_path))
        except:
            pass
        # if z[0] == '.':
        #     image.save(os.path.join('thumbnails', x), "jpeg")
        # else:
        image.save(os.path.join('thumbnails', cwd_path, x), "jpeg")



