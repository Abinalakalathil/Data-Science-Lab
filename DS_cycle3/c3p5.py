#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:39:51 2021

@author: sjcet
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["walking", "cycling", "car", "bus","train"])
y = np.array([29,15,35,18,3])

plt.bar(x,y, color="#4CAF50",width=0.1)
plt.show()