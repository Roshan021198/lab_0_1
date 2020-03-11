# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:32:30 2020

@author: ROSHAN
"""
import string
s = input("enter string = ")

words = s.split(" ")

s1=[]

for word in words:    
    s1.append(word)

print(string.capwords(" ".join(s1)))

s1 = input("enter string")
list = [' '.join(word[0].upper() + word[1:] for word in s.split())]
print(" ".join(list))