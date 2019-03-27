#coding=utf-8
'''
Created on 2018年10月8日

@author: Tianxiaomo
'''
import numpy as np
import Hutil.np

def D(x):
    x = Hutil.np.flatten(x)
    return np.var(x)

def E(x):
    x = Hutil.np.flatten(x)
    return np.average(x)
