# -*- coding: utf-8 -*-
'''
有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

2017-05-17 
Jing Qin
'''

from PIL import Image as img
import os
import os.path
import sys
import re

def run(path_file): #get all pictures from folder
    imgTypes = ['.png','.jpeg','.bmp','.JPG']
    pattern = re.compile('(.*\/).*')
    path = re.findall(pattern,path_file)[0]
    for root, dirs, files in os.walk(path):
        for name in files:
            if os.path.splitext(name)[1] in imgTypes:
                img_file = img.open(path + name)
                process_image(img_file,os.path.splitext(name),path)

def process_image(img,name,path): # resize pics to 640*1136(or smaller)
    img_w,img_h = img.size
    rate = max(img.size[0]/640.0 if img.size[0] > 640 else 0, img.size[1]/1136.0 if img.size[1] > 1136 else 0)
    # get a rate for resize
    if rate:
        img.thumbnail((img.size[0]/rate, img.size[1]/rate))
    img.save(path + name[0]+"resize"+".jpeg", "jpeg")            

if __name__ == '__main__':
    run(sys.argv[1])   