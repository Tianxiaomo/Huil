#!/usr/bin/env python
# encoding: utf-8
'''
@author: tianxiaomo
@license: (C) Apache.
@contact: huguanghao520@gmail.com
@software: 
@file: pil.py
@time: 2019/3/26 13:55
@desc:
'''
from PIL import Image
import numpy as np

def transparent_back(img,color):
    '''
    透明画背景
    :param img:
    :return:
    '''
    img = img.convert('RGBA')
    L, H = img.size
    color_0 = img.getpixel((0,0))
    img = np.asarray(img)
    p = (img[:,:,:3] == color)
    p = p.astype('uint8')
    p = p.sum(axis = -1)
    p = (p!=3).astype('uint8')
    img_1 = img.copy()
    img_1[:,:,-1] = p*255
    img_1 = Image.fromarray(img_1)
    return img_1