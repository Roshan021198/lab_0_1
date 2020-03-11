# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:03:55 2020

@author: ROSHAN
"""

s = input("enter string = ")

words = s.split(" ")
s1=[]
for word in words:
    s1.insert(0,word)

print(" ".join(s1))