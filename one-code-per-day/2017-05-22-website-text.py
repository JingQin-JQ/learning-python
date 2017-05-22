# -*- coding: utf-8 -*-
'''
一个HTML文件，找出里面的正文。

2017-05-22 
Jing Qin
'''

from goose import Goose
# from goose.text import StopWordsChinese     for Chinese website only
import sys

#url = "https://www.marktplaats.nl/a/diensten-en-vakmensen/restaurants-en-cateraars/a1006096961-lichtreclame-led-lichtbak-stoepbord-reclamebord.html?c=e757dd852a9085e505d6b1572f83e8d0&previousPage=HOMEPAGE_NEW_AND_POPULAR"

def run(url):
    '''
    Get "url" as arguments of function "run",
     find html file, use goose to get text.
    '''
    g = Goose()
    # g = Goose({'stopwords_class': StopWordsChinese}) it can support Chinese when include this line.
    article = g.extract(url=url)
    print article.cleaned_text,"@@@title:", article.title,"@@@description:", article.meta_description, "@@@image:",article.top_image.src
    # print not only the txt,also title, description and image.

if __name__ == '__main__':
    run(sys.argv[1])