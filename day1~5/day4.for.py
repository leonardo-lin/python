# -*- coding: utf-8 -*-
"""
Created on Fri May 22 22:36:45 2020

@author: leo
"""
x=0
a=0

for a in range(10): #range為一陣列[0,1,...,9],a每次從range的第i格提取資料
    a = a+4
    #a=1
    x+=a
    print("a=",a,"x=",x)
    

    
print(x)

"""
q=int(input())

for i in q:
    if q%i==0:
        print('是質數')
        
"""   



