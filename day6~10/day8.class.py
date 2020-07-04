# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 14:10:16 2020

@author: leo
"""
"""self有點像this的一思"""
"""other則是可以呼叫其他class來做比較之類的"""
class Student(object):
    n='test'
    """放在這裡乎也可,呼叫時+self"""
    def __init__(self,name,age):#直接呼叫(那個叫啥我忘了)
        self.name = name
        self.age = age
        self.b=age
        #n=age
    def __pri(self,course_name):   
        
        print('%%%%%% %s' % ( course_name))
    def study(self, course_name):
        """"""
        k = Student('name',10)
        k.__pri('AAAA')
        """class內部可直接呼叫其他函數"""
        print(self.b,'歲',self.n)
        print('%s正在學習%s' % (self.name, course_name))
    def watch_movie(self):
        if self.age < 18:
            print('%s只能觀看frozen' % self.name)
        else:
            print('%s正在觀看片片' % self.name)
 
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')  


"""時鐘練習"""
from time import sleep
class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """顯示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)
def main():

    stu1 = Student('楊毅',15)    
    stu1.study('Python爬蟲')
    stu1.__init__('楊毅', 38)    
    stu1.watch_movie()
    """class需要這樣呼叫private的函數"""
    stu1._Student__pri('qqq')    
    """"""
    stu2 = Student('子安', 15)    
    stu2.study('思想品德')
    stu2.watch_movie()
    #前面加__是private
    #test = Test('hello')    
    #test.__bar()   
    #print(test.__foo)
    
    
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

"""!!!"""
if __name__ == '__main__':
    main()    
  
        
        
        
        
        
        
        
        
        
        
        
        