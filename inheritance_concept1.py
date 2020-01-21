##class A:
##    def fun(self):
##        print("Hi!")
##
##class B(A):
##    def fun2(self):
##        print("Hello!")
##b = B()
##b.fun()
##b.fun2()
##

####Single Inheritance
class Parent:
    def m1(self):
        print("Parent method")

class Child(Parent):
    def m2(self):
        print("Child method")

c = Child()
c.m1()
c.m2()
