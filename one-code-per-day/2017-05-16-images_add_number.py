# -*- coding: utf-8 -*-
'''
将一张图片右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

2017-05-16 
Jing Qin
'''

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import sys
import re



def add_number(path_file):
    '''
    Get a file with its path as arguments of function "add_number",
     use draw.txt to add a txt on to the image, 
     and save the new image to the same location.
     '''
    im = Image.open(path_file)
    
    pattern = re.compile('(.*\/).*')
    path = re.findall(pattern,path_file)[0]
    # get a jpeg file
    font = ImageFont.truetype('/System/Library/Fonts/Apple Symbols.ttf', 50) 
    #get a font type file,and size 
    draw = ImageDraw.Draw(im) 
    #get a draw object
    w,h = im.size 
    draw.text((w-50,0), "8", (255,0,0), font=font)
    # locate "8" at right-up corner
    im.save((path+"add number.jpeg"), "jpeg") 

if __name__ == '__main__':
    add_number(sys.argv[1]) 