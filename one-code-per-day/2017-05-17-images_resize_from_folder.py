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

def run(directory): #get all pictures from folder
    '''
    Get "directory" as arguments of function "run",
     find all image file which have their type in "img_types" , 
     call function "process_image" to resize them.
     '''
    img_types = ['.png','.jpeg','.bmp','.JPG']
    for root, dirs, files in os.walk(directory):
        for name in files:
            if os.path.splitext(name)[1] in img_types:
                img_file = img.open(directory+"/" + name)
                process_image(img_file,os.path.splitext(name),directory)

def process_image(img,name,directory): # resize pics to 640*1136(or smaller)
    '''
    Get "img", "name"and "directory" as arguments of function "process_image",
     resize images to 640*1136 or smaller, and keep their own w/h ratio.
     save new images to the same directory with "_resize" added to their old name.
     '''
    img_w,img_h = img.size
    rate = max(img_w/640.0 if img_w > 640 else 0, img_h/1136.0 if img_h > 1136 else 0)
    # get a rate for resize
    if rate:
        img.thumbnail((img_w/rate, img_h/rate))
    img.save(directory+ name[0]+"_resize"+".jpeg", "jpeg")            

if __name__ == '__main__':
    run(sys.argv[1])   