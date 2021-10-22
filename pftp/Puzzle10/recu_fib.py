#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 09:16:23 2021

@author: toku
"""

# test of test 

def rFib(x):
    if x < 2:
        return x
    else:
        f, g = 0, 1
        for i in range(x-1):
            f, g = g, f + g
        return g

fi = rFib(1000)
print (fi)

