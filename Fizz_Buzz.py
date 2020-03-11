# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 00:28:00 2020

@author: ROSHAN
"""

#divided by 2 fizz & divided by 3 buzz
n = int(input("enter a number = "))
if(n%2==0):
    print("FIZZ")
elif(n%3==0):
    print("BUZZ")
else:
    print("FIZZ_&_BUZZ")