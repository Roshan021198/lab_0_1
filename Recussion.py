# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:17:12 2020

@author: ROSHAN
"""

def fact(n):
    if n==0:
        return 1
    else:
        return (fact(n-1)*n)

a = int(input("enter a number to find the factorial = "))
print(fact(a))