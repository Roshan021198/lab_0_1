# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 00:34:02 2020

@author: ROSHAN
"""

s = input("Enter a character: ")
count=0
for ch in range(0,len(s)):
    if(s[ch]=='A' or s[ch]=='a' or s[ch]=='E' or s[ch] =='e' or s[ch]=='I'or s[ch]=='i' or s[ch]=='O' or s[ch]=='o' or s[ch]=='U' or s[ch]=='u'):
        count+=1
print("numbers of vowels" ,count)
    




