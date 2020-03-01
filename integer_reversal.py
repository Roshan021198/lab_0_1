# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:44:39 2020

@author: ROSHAN
"""

n=int(input("enter a number \t "))
rev=0

while n!=0:
    rev=rev*10+n%10
    n=n//10

print(rev)