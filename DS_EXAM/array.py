#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 13:51:18 2022

@author: sjcet
"""
import numpy as np
a=np.arange(1,41,2)
dtype=float()
print(a)
print("No.of rows and columns=",a.shape)
a = a.reshape(5,4)
print(a)
print("Display the elements of rows 2 to 5 and columns 1 to 3")
print(a[1:,:3])
print("Display the elements of 2 nd and 3 rd column")
print(a[:,1:3])
print("Display last 2 elements of last row")
print(a[4:,2:])