# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:54:04 2020

@author: Admin
"""

import random
n=int(input("Nhập n= "))
R=random.sample(range(1,50),n)
print("List ngẫu nhiên là",R)
M=0
M=int(M)
i=0
i=int(i)
while i<n:
    if M<R[i]:
        M=R[i]
    i+=1       
print("Giá trị lớn nhất là",M)