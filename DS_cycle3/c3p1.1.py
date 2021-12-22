#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:10:59 2021

@author: sjcet
"""
from matplotlib import pyplot as plt
  
x = [2001, 2002, 2003,2004,2005,2006,2007]
  
y = [2400, 22500, 19700,17500, 14500,10000,5800]
  

  
plt.title("value depreciation",loc='left')

plt.plot(x,y,'r', linestyle='dashdot', linewidth=3)
plt.plot(x,y, '*',color = 'green',ms='20')
plt.show()
