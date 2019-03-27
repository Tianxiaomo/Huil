#!/usr/bin/env python
# encoding: utf-8
'''
@author: tianxiaomo
@license: (C) Apache.
@contact: huguanghao520@gmail.com
@software: 
@file: __init__.py
@time: 2019/3/17 16:29
@desc:
'''
from Hutil import log
from Hutil import dtype
from Hutil import plt
from Hutil import np
from Hutil import img

_img = img
from Hutil import dec
from Hutil import rand
from Hutil import mod
from Hutil import proc
from Hutil import test
from Hutil import neighbour as nb
# from Hutil import mask
from Hutil import str_ as str
from Hutil import io_ as io
from Hutil import feature
from Hutil import thread_ as thread
from Hutil import caffe_ as caffe
from Hutil import tf
from Hutil import cmd
from Hutil import ml
from Hutil import url
from Hutil import time_ as time
from Hutil.progress_bar import ProgressBar
import io as sys_io
import sys


# log.init_logger('~/temp/log/log_' + get_date_str() + '.log')

def exit(code=0):
    sys.exit(0)


is_main = mod.is_main
init_logger = log.init_logger


def get_temp_path(name=''):
    _count = get_count();
    path = '~/temp/no-use/images/%s_%d_%s.png' % (log.get_date_str(), _count, name)
    return path


def sit(img=None, format='rgb', path=None, name=""):
    if path is None:
        path = get_temp_path(name)

    if img is None:
        plt.save_image(path)
        return path

    if format == 'bgr':
        img = _img.bgr2rgb(img)
    if type(img) == list:
        plt.show_images(images=img, path=path, show=False, axis_off=True, save=True)
    else:
        plt.imwrite(path, img)

    return path


_count = 0;


def get_count():
    global _count;
    _count += 1;
    return _count


def cit(img, path=None, rgb=True, name=""):
    _count = get_count();
    if path is None:
        img = np.np.asarray(img, dtype=np.np.uint8)
        path = '~/temp/no-use/images/%s_%s_%d.jpg' % (name, log.get_date_str(), _count)
        _img.imwrite(path, img, rgb=rgb)
    return path


argv = sys.argv

