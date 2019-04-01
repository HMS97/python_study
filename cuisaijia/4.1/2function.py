#!/usr/bin/env python
# coding: utf-8
# -*- coding: utf-8 -*-

import numpy as np

m=[10,20,30]
n={'Bob':80,'Mary':90,'Jack':76}


def adds():
    s=0
    right=1
    while(right==1):
        mod=input('请输入模式 1 or 2:   ')
        mode=int(mod)
        if((mode == 1 )or( mode == 2)):
            right=0
    if mode == 1:
          for i in range(len(m)):
            s=s+m[i]
    else:
          s=sum(n.values())          
    print(s)
    return s


adds()

