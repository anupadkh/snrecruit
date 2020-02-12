def find_slider(tagged):
    # print(tagged)
    for a, b in tagged:
        # print(str(a))

        if str(a) == "home-slider":
            # print(b[0].content)
            return b

    return []

import re

def make_list(articles, pages, category, tags):
    file = open('list_of_articles.json','w')
    mylist = {}
    articl = {}
    for y in articles:
        if y.stitle != None:
            articl[str(y.slug)] = {'stitle':y.stitle,'icon':'', 'url':y.url, 'title':y.title}

        else:
            articl[str(y.slug)] = {'stitle':y.title,'icon':'', 'url':y.url, 'title':y.title}
        try:
            articl[str(y.slug)]['icon'] = y.icon
        except:
            pass
    mylist['articles'] = articl
    # print(mylist)
    # print(y.__dict__)

    articl = {}

    for y in pages:
        if y.stitle != None:
            articl[str(y.slug)] = {'stitle':y.stitle,'icon':'', 'url':y.url, 'title':y.title}
        else:
            articl[str(y.slug)] = {'stitle':y.title,'icon':'', 'url':y.url, 'title':y.title}
        try:
            articl[str(y.slug)]['icon'] = y.icon
        except:
            pass

    mylist['pages'] = articl
    # print(mylist)

    cats = {}
    for y,m in category:
        articl = []
        for z in m:
            articl.append(z.slug)
        cats[str(y)] = articl
    mylist['categories'] = cats
    # print(mylist)

    taggeds = {}
    for y,m in tags:
        articl = []
        for z in m:
            articl.append(z.slug)
        taggeds[str(y)] = articl
    mylist['tags'] = taggeds
    # print(mylist)
    file.write(str(mylist))
    file.close()
    print(m[0].save_as, m[0].url, m[0].slug, m[0].source_path, m[0].date)
    return ''

def strip_tags(text):
    return re.sub('<[^<]+?>', '', text)

class myImage:
    title = ''
    path = ''
    meta = ''

    def __init__(self, title, path, meta=None):
        if meta == None:
            self.title = title
            self.path = path
            if self.meta != None:
                self.meta = meta
        

def findimagelist(articles,slug):
    for y in articles:
        if y.slug == slug:
            images = []
            try:
                images_title = y.images_title.split(',')
                # print(images_title)
            except:
                return y.images_list.split(',')
            images_path = y.images_list.split(',')
            for x in range(len(images_path)):
                images.append(myImage(title=images_title[x], path=y.image_path + images_path[x]))
            # print (images)
            return images
    return []

def findbyslug(articles, slug):
    for y in articles:
        if y.slug == slug:
            return y
    return None


def findbytag(articles, tag):
    collection = []
    
    for y in articles:
        try:
            if  tag in y.tags :
                collection.append(y)
                print(y.title)
        except:
            pass
    return collection


def see(value):
    print("Sarkar" + value)
    return value

def findarticle(articles, tag=None, category=None):
    z = []
    for y in articles:
        if tag == None:
            try:
                if (y.category == category):
                    z.append(y)
            except:
                pass
        elif category == None:
            try:
                if y.tag == tag:
                    z.append(y)
            except:
                pass
        else:
            try:
                if (y.tag == tag) & (y.category == category):
                    z.append(y)
            except:
                pass
    return z
