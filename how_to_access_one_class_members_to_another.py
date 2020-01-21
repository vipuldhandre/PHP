##class A:
##    num1, num2 = 100,200
##
##class B:
##    def add(self):
##        a = A()
##        print(f'Addition is {a.num1+a.num2}')
##    def mul(self):
##        a = A()
##        print(f'Multiplication is {a.num1*a.num2}')
##
##b = B()
##b.add()
##b.mul()
##                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
class A:
    num1, num2 = 100,200

class B:
    a = A()
    def add(self):
        
        print(f'Addition is {self.a.num1+self.a.num2}')
    def mul(self):
        
        print(f'Multiplication is {self.a.num1*self.a.num2}')

b = B()
b.add()
b.mul()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
