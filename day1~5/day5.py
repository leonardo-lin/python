# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:48:10 2020

@author: leo
"""
num=0
"""
自幂数
"""
for num in range(100,1000):
        temp=num
        #print(temp)
        low = temp%10
        temp=temp//10
        mid =temp%10
        temp=temp//10
        high =temp%100
        #print('%d %d %d'%(low ,mid ,high))
        #print(num)
        if num == (low ** 3 + mid ** 3 + high ** 3):
            print(num)
            
#num = int (input('num='))
"""
字串反轉
"""
num= 'qwertyui'
numm = list(num)
print(numm[::-1])


"""
while 識字反轉
"""
num=13579
rer =0
i=1
while num>0:
    rer=(rer*10) + num%10
    num=num//10
print(rer)

"""
百钱百鸡
"""
#公雞5元 母雞3元 小雞3隻1元
#100元有100隻雞
for x in range (0,20):
    for y in range(0,33):
        z= 100-x-y
        #print( z,y,z)
        if (5*x +3*y +z/3)==100 and z%3==0:
            print( x,y,z)

"""
random基數偶數
"""
from random import randint
import random
dise = randint(1, 6)
print(dise)
#give = int(input('猜基數偶數整能輸入1&2'))
give =2
if (dise%2==0 and give==2) or dise%2!=0 and give!=2:
    print('youwin' , dise)
else:
    print('youlose' ,dise)

v=random.choice([1,2,3,4,5,6])
print(v)



