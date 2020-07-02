# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:00:22 2020

@author: leo
"""
"""版本控制"""
"""函數依定要放在使用前"""

"""函數使用及全域變數"""
"""函數中函數可直接使用外層函數的所有東西"""
n= 4#int(input())

def multi(num):
    
    global n,m #宣告會使用到全域變數   
    print("n=",n,"m=",m)
   
    def inside():
        print(ans,n,m)
    
    ans=1
    inside()
    
    for n in range(1,num+1):
        ans=ans*n
    n=6   
    return ans

m= 4#int(input())
print(multi(n),"全域變數改變",multi(m))
print(n,"全域變數受到函數改變")

#import random
"""不依順序輸入"""
def rolldice(n=2):
    re=0
    for i in range(0,n):
        #re=re+random.uniform(1,6)
        re+=1
    return re

print(rolldice(),"沒有輸入直進去")
print(rolldice(3),"輸入3進去")

def three(a=0,b=0,c=0):
    print(a,b,c)
    
three()
three(1,2,3)
three(c=1,b=2,a=3)

"""輸入指標類陣列(可不限變數或陣列)"""
def add(*args):
    ans=0
    #print(len(args))
    for i in args:
        ans+=i
    return ans

print(add())
print(add(1))
print(add(1,2,3,4,5))

"""輸入陣列"""
def tr(arg):
    ans=0
    for i in arg:
        ans+=i
    return ans
q=[1,2,30]
b=[]
c=2
print(tr(q))
print(tr(b))

"""同名函數後面會覆蓋前面"""
""""也套用在import別人的"""
def foo():
    print('hello, world!')
def foo():
    print('goodbye, world!')
foo()

"""from day5 import function"""
"""import day5 as d5以後使用只要呼叫d5即可"""

"""練習回文"""
def palin(s):
    l=len(st)
    l=l-1
    i=0
    while i<l/2:
        if (s[i]!=s[l-i]):
            return False
        i+=1
    return True

st="123456654321"
print(palin(st))
        
        







    
    
