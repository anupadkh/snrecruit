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
