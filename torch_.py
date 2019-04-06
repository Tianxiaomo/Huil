#!/usr/bin/env python
# encoding: utf-8
'''
@author: tianxiaomo
@license: (C) Apache.
@contact: huguanghao520@gmail.com
@software: 
@file: torch_.py
@time: 2019/3/28 22:31
@desc:
'''

from tqdm import tqdm
import time

total = 10000  # 总迭代次数
loss = total
with tqdm(total=total, desc='Train Epoch:{}'.format(1)) as pbar:
    for i in range(total):
        '''
        模型训练
        '''

        loss -= 1
        pbar.set_postfix({'loss': '{0:1.5f}'.format(loss)})  # 输入一个字典，显示实验指标
        pbar.update(1)
        time.sleep(1)
