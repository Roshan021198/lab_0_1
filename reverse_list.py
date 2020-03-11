# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 00:47:12 2020

@author: ROSHAN
"""
list=[]
n = int(input("ernter the no of elements in list "))
for i in range(0,n):
    ele=int(input("enter element in "+str(i) +" position = "))
    list.append(ele);

print("normal list)
print(list)
print("reversed list")
print(list[::-1])