#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 09:16:23 2021

@author: toku
"""

# test of test 

def rGcd(m, n):
    print("initial def   ", m, n, m % n)
    if m % n == 0:
        print("when zero  ", n, "m= ", m)
        return n
    else:
        gcd = rGcd(n, m % n)
        print("gcd = ", gcd ,"  else    ", m, n, m % n)
        return gcd

print(rGcd(2002, 1344))
    