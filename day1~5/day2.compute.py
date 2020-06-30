
a=9
b=2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)#除成整數
print(a % b)
print(a ** b)
print(  )


a = 100
b = 3.1415926
c = 1 + 5j
d = 'hello, world'
e = True
f= "f"
print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'complex'>
print(type(d)) # <class 'str'>
print(type(e)) # <class 'bool'>
print(  )

print(chr(a))
print(float(a))
print(ord('f'))#強制轉型數字
print(int('46',8))#把46轉成10進位
print('%d %c %f'%(a,a,a))
#print(unichr(65))
"""
input
"""
#a= int(input('a='))#限定數字
#b=input('who?')
print(a)
print(b)

#kf=float(input('please input temperature '))
kf=40
kc=(kf-32)/1.8
print(kc)

#r=float(input('please input 半徑: 周常半徑'))
import math
""""""
r=10
per =  r*2* math.pi
area = r*r* math.pi
print(per,area)

#year=int(input('please input year  閏年問題'))
year=2000
if((year%4==0 and year%100!=0)or(year%400==0)):
    print('TRUE')
else:
    print('FALSE')





