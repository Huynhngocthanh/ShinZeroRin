# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:52:41 2020

@author: Admin
"""

import random
print("Nhập ngẫu nhiên số phần tử trong list")
n=int(input("Nhập n="))
T=random.sample(range(1,100),n)
print("List ngẫu nhiên là",T)
m=100000
m=int(m)
i=1
i=int(i)
while i<n:
    if m>T[i]:
        m=T[i]
    i+=1
print("Giá trị nhỏ nhất là",m)