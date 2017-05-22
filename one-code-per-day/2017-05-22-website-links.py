# -*- coding: utf-8 -*-
'''
一个HTML文件，找出里面的链接。

2017-05-22 
Jing Qin
'''

import urllib
import re
import sys

#url = "https://www.marktplaats.nl/a/diensten-en-vakmensen/restaurants-en-cateraars/a1006096961-lichtreclame-led-lichtbak-stoepbord-reclamebord.html?c=e757dd852a9085e505d6b1572f83e8d0&previousPage=HOMEPAGE_NEW_AND_POPULAR"



def run(url):
    '''
    Get "url" as arguments of function "run",
     find html file, use regular experesion to get links.
    '''
    html = urllib.urlopen(url).read()
    links = re.findall('"(http://.*?)"', html)
    for e in links:
        print e

if __name__ == '__main__':
    run(sys.argv[1])


