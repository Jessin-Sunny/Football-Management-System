# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:18:13 2021

@author: Sunny John
"""
import random
d={1:"GERMANY",2:"TURKEY",3:"POLAND",4:"ENGLAND",5:"CROATIA",6:"ITALY"}
d1=d
x=random.randint(1,3)
y=random.randint(1,3)
c=True
if x==y:
    c=False
else:
    while c:
        print(d1[x],"\t\tvs\t\t",d1[y])
        d1.pop(x)
        d1.pop(y)
        c=False
    
    
