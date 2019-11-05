def find_slider(tagged):
    # print(tagged)
    for a, b in tagged:
        print(str(a))

        if str(a) == "home-slider":
            print(b[0].content)
            return b

    return []

import re
def strip_tags(text):
    return re.sub('<[^<]+?>', '', text)

def findbyslug(articles, slug):
    for y in articles:
        if y.slug == slug:
            return y
    return None

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
