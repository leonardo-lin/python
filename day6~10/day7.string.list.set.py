# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:05:01 2020

@author: leo
"""

s='\141\142\143\x65\x62\x63'
s1='AAA'*3 #s1=AAAAAAAAA
s2= 'BBB'+s1 #s2=BBBAAAAAAAAA
print(s1,s2)
print('B' in s1,'B'in s2)
s3='123456789'
print(s3[0])
print(s3[1:-1])
print(s3[1::2])
print(s3[len(s3)::-1])#倒敘
print(s3[-8:22:2])#超過沒差
print(s3.find('67'))
"""len,upper,title,startswith,endwith,center,isdigit,isalpha,isalnum,strip """
for i in range(len(s1)):
    print(s1[i],end='')
print('')
print('')

s4=['qqqq','wwww']
list1=[1,3,9]
list1.append(200)
list1.insert(1, 300)
list1=list1+[s1,s4]
print(list1)
list1.pop(0)
print(list1)
list1.clear()
print('')

f =[0 for x in range(5)]
print(f)

g=tuple(f)
print(g)
print('')

set4 = {num for num in range(1, 100) if num % 5 == 0}
print(set4)
print('')

#set1=set(range(1,10))
#print(set1)
set3 = set((1,1,2,2,3,3,4,4,5,6))
print(set3)
set4 = set((5,6,7,8))
set5 = set((5,6))
print((set3 & set4))
print(set3 | set4)
print(set3-set4)
print(set3 ^ set4)
print(set3 >= set4)
print(set3 >=set5)
print("")

"""hashmap(?"""
hashs = {'A':65,'B':66,'C':67}
hashs['D']=68
print(hashs['A'],hashs['C'],hashs['D'])
print(hashs.get('E'))
print(hashs)
print(hashs.popitem())

items3 = {num: num ** 2 for num in range(1, 10)}
print(items3)








