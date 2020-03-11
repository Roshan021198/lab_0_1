# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:31:01 2020

@author: ROSHAN
"""

n=int(input("enter a number \t "))
sum=0
n1=n
print(n1)

while n!=0:
    sum=sum*10+n%10
    n=n//10
    
if n1==sum:
    print("palindrom")
else:
    print("not")