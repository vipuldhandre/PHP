
##def display1():
##    for _ in range(10):
##        print("Child Thread")
##display1()
##for _ in range(10):
##    print("Main Thread")

##def display1():
##    for x in range(10):
##        print(f"Child Thread:{x}")
##display1()
##for x in range(10):
##    print(f"Main Thread:{x}")



##import threading *
##import time
##def display1():
##    time.sleep(1)
##    for x in range(10):
##        print(f"name of current thread for display1()",threading.current_thread().getName())
##    print("*"*40)
##starttime = time.time()
##        
##display1()
##for x in range(10):
##    time.sleep(1)
##    print(f"name of current thread for looping",threading.current_thread().getName())
##endtime = time.time()
##print("Total time required to execute a program:",endtime-starttime)


##from threading import *
##import time
##def display1():
##    
##    for x in range(10):
##        time.sleep(0.4)
##        print("name of current thread for display1():",current_thread().getName())
##    
##starttime = time.time()
##
##t = Thread(target = display1)
##t.start()        
##
##for x in range(10):
##    time.sleep(0.8)
##    print("name of current thread for looping:",current_thread().getName())
##endtime = time.time()
##print("Total time required to execute a program:",endtime-starttime)



##import time
##from threading import *
##def sq(l):
##    print("Name of the current thread for sq(l):",current_thread().getName())
##    for x in l:
##        print(f'Square of {x} is {x**2}')
##
##def cube(l):
##    print("Name of the current thread for cube(l):",current_thread().getName())
##    for x in l:
##        print(f'Cube of {x} is {x**3}')
##begintime = time.time()
##l = [1,2,3,4,5,6,7,8,9]
##sq(l)
##print("*"*50)
##cube(l)
##endtime = time.time()
##print("Total time required to execute a program:",endtime-begintime)


##import time
##from threading import *
##def sq(l):
##    print("Name of the current thread for sq(l):",current_thread().getName())
##    for x in l:
##        print(f'Square of {x} is {x**2}')
##
##def cube(l):
##    print("Name of the current thread for cube(l):",current_thread().getName())
##    for x in l:
##        print(f'Cube of {x} is {x**3}')
##begintime = time.time()
##l = [1,2,3,4,5,6,7,8,9]
##t1 = Thread(target = sq,args = (l,))
##t2 = Thread(target = cube,args = (l,))
##
##t1.start()
##
##t2.start()
##
##t1.join()
##t2.join()
##endtime = time.time()
##print("Total time required to execute a program:",endtime-begintime)

##import time
##from threading import *
##l = eval(input("Enter the list elements:"))
##def sq(l):
##    print("Name of the current thread for sq(l):",current_thread().getName())
##    for x in l:
##        print(f'Square of {x} is {x**2}')
##
##def cube(l):
##    print("Name of the current thread for cube(l):",current_thread().getName())
##    for x in l:
##        print(f'Cube of {x} is {x**3}')
##begintime = time.time()
##
##t1 = Thread(target = sq,args = (l,))
##t2 = Thread(target = cube,args = (l,))
##
##t1.start()
##
##t2.start()
##
##t1.join()
##t2.join()
##endtime = time.time()
##print("Total time required to execute a program:",endtime-begintime)


##from threading import *
##import time
##class A(Thread):
##    def sq(self,l):
##        print("Name of the current thread for sq(l):",current_thread().getName())
##        for x in l:
##            print(f'Square of {x} is {x**2}')
##            time.sleep(1)
##    def run(self):
##        self.sq(l)
##l = [1,2,3,4,5,6,7]
##t = A()
##
##t.start()
##t.join()


##import threading,time
##class MyClass(threading.Thread):
##    def __init__(self,ThreadID,name,count):
##        threading.Thread.__init__(self)
##        self.ThreadID = ThreadID
##        self.name = name
##        self.count = count
##
##    def run(self):
##        print(f'ThreadId:{self.ThreadID},Name:{self.name},Count:{self.count}\n')
##begintime = time.time()
##t = MyClass(1,'Vipul',10)
##t1 = MyClass(2,'Vikas',20)
##t.start()
##t1.start()
##t.join()
##t1.join()
##endtime = time.time()
##print("Total time required is:",endtime-begintime)
            
##import threading,time
##class MyClass(threading.Thread):
##    def __init__(self,ThreadID,name,count):
##        threading.Thread.__init__(self)
##        self.ThreadID = ThreadID
##        self.name = name
##        self.count = count
##
##    def run(self):
##        print("Name of current thread is:",threading.current_thread().getName())
##        for x in range(10):
##            time.sleep(1)
##            print(f'ThreadId:{self.ThreadID},Name:{self.name},Count:{self.count}\n')
##begintime = time.time()
##t = MyClass(1,'Vipul',10)
##t1 = MyClass(2,'Vikas',20)
##t.start()
##t1.start()
##t.run()
##t1.run()
##t.join()
##t1.join()
##endtime = time.time()
##print("Total time required is:",endtime-begintime)        
        
##from threading import *
##t = current_thread()
##print(current_thread().getName())
##print(t.isDaemon())
    
##from threading import *
##
##def fun1():
##    print("name of current thread is:",current_thread().getName())
##t = Thread(target = fun1)
##t.start()
##t.join()
##print(t.isDaemon())


##from threading import *
##class A:
##    def fun1(self):
##        print("Name of current thread is:",current_thread().getName())
##        
##obj = A()
##t1 = Thread(target=obj.fun1)
##t1.start()
##t1.join()
##print(t1.isDaemon())

##from threading import *
##def function1():
##    print("name of the current thread:",current_thread().getName())
##t1 = Thread(target = function1)
##t1.setDaemon(True)
##t1.start()
##t1.join()
##print("name of current thread:",current_thread().getName())
##print("Is current thread Daemon?:",t1.isDaemon())

##from threading import *
##def m1():
##    print("Execute by t1 thread")
##    t2 = Thread(target = m2)
##    t2.start()
##    t2.join()
##    print('Thread of m1():',t2.isDaemon())
##def m2():
##    print("Execute by t2 thread")
##    
##t1 = Thread(target = m1)
##t1.start()
##t1.join()
##print("Thread of m2()",t1.isDaemon())

from threading import *
def m1():
    print("Execute by t1 thread")
    t2 = Thread(target = m2)
    t2.start()
    t2.join()
    print('Thread of m1():',t2.isDaemon())
def m2():
    print("Execute by t2 thread")
    
t1 = Thread(target = m1)

t1.setDaemon(True)
t1.start()
t1.join()
print("Thread of m2()",t1.isDaemon())
