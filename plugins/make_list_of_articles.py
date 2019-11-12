# make_list_of_articles.py

from pelican import signals
import pelicanconf as settings
import json

def test(generator, content):
    try:
        file = open('list_of_articles.json','r+')
        dict = json.load(file)
    except:
        file = open('list_of_articles.json','w')
        dict = {'articles':{},'pages':{}, 'categories':{}, 'tags':{}}

    id = content.metadata.get('slug', "")
    title = content.metadata.get('title', "")
    icon = content.metadata.get('icon',"")
    stitle = content.metadata.get('stitle', "")

    dict['articles'][id] = {
        'url':settings.ARTICLE_SAVE_AS.format(slug=id),
        'stitle':stitle,
        'icon':icon,
        'title':title,
    }
    file.seek(0)
    json.dump(dict,file,indent=4)
    file.truncate()
    file.close()
    # print ( filename + " initialized !!")

def test_page(generator, metadata):
    try:
        file = open('list_of_articles.json','r+')
        dict = json.load(file)
    except:
        file = open('list_of_articles.json','w')
        dict = {'articles':{},'pages':{}, 'categories':{}, 'tags':{}}

    id = metadata.get('slug', "")
    title = metadata.get('title', "")
    icon = metadata.get('icon',"")
    stitle = metadata.get('stitle', "")

    dict['pages'][id] = {
        'url':settings.PAGE_SAVE_AS.format(slug=id),
        'stitle':stitle,
        'icon':icon,
        'title':title,
    }
    file.seek(0)
    json.dump(dict,file,indent=4)
    file.truncate()
    file.close()

def test_content(content_object):
    try:
        # print( str(content_object.metadata.get('title', "None")) + ""  )
        mystr = content_object.metadata.get('slug', '404')
        total = settings.ARTICLE_SAVE_AS
        print(total.format(slug=mystr))
    except:
        print (str(content_object.metadata))

def myfinals(object):
    # print(object.__dict__)
    pass

def register():
    signals.article_generator_write_article.connect(test)
    signals.page_generator_context.connect(test_page)
    # signals.content_object_init.connect(test_content)
    signals.finalized.connect(myfinals)
