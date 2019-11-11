def merge(a,b):
    c = a.copy()
    c.update(b)
    return c

def article_get(slug):
    print(slug)
    file = open('list_of_articles.json', 'r')
    all = eval(file.read())
    file.close()
    articles = all['articles']
    articles.update(all['pages'])
    return articles[slug]


def return_menu(y=None):
    file = open('list_of_articles.json', 'r')
    all = eval(file.read())
    file.close()
    file = open('self.json', 'r')
    others = eval(file.read())
    file.close()
    file = open('menu.json', 'r')
    menu = eval(file.read())
    file.close()
    articles = merge(all['articles'], all['pages'])
    articles = merge(articles, others)
    new_dict = {}
    for key, value in menu['main']['parents'].items():
       if value in new_dict:
           new_dict[value].append(key)
       else:
           new_dict[value]=[key]
    menu_children = new_dict
    menu_items = {}

    for x in menu['main']['items']:
        menu_items[x] = articles[x]
        if x in menu_children.keys():
            menu_items[x]['child'] = menu_children[x]
    print(menu_items)
    return menu_items.items()
