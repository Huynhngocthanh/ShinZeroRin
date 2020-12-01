# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:15:27 2020

@author: Admin
"""

import string,random
R=dict()
n=random.randrange(1,15)
T=random.choice(string.ascii_uppercase)
H=T+''.join(random.choice(string.ascii_lowercase) for i in range(n-1))
R['name']=H
A=random.randrange(1,100)
R['age']=A
print("Dictionary: ",R)
