# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:12:27 2019

@author: Sampad Acharya
"""

for i in  range(1,1000):
  S=[]
  for j in range(1,i):
    div= i%j
    S.append(div)
#  print(i)
#  print(S.count(0))
  if S.count(0)==1:
    print(i, 'is prime')  
