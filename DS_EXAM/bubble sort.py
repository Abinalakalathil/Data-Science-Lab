#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:31:18 2022

@author: sjcet
"""

def bubble_sort(list1):
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if (list1[j] > list1[j + 1]):
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return list1
n = int(input("Enter the size of the list: "))
list1 = list(int(num) for num in input("Enter the elements:").strip().split())[:n]
print("The unsorted list is: ", list1)
print("The sorted list is: ", bubble_sort(list1))
