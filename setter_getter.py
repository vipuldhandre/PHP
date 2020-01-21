##class Student:
##    def setname(self,name):
##        self.name = name
##    def getname(self):
##        return self.name
##
##    def setmarks(self,marks):
##        self.marks = marks
##    def getmarks(self):
##        if self.name == "Kiran":
##            return self.marks
##
##obj = Student()
##obj.setname("Vipul")
##print(obj.getname())
##obj.setmarks(100)
##print(obj.getmarks())
##
##        
        
##class Employee:
##    def __init__(self,id,salary):
##        self.id = id
##        self.salary = salary
##    def display(self):
##        print(f'ID:{self.id} your salary is {self.salary}')
##        
##obj = Employee(1,100000)
##obj.display()

##class Employee():
##    def setid(self,id):
##        self.id = id
##    def getid(self):
##        return self.id
##
##    def setsalary(self,salary):
##        self.salary = salary
##    def getsalary(self):
##        return self.salary
##
##obj = Employee()
##obj.setid(1)
##obj.setsalary(100000)
##print("Id:",obj.getid())
##print("Salary",obj.getsalary())
##

class Employee:

    companyname = "CISCO"

    def __init__(self,id,salary):
        self.id = id
        self.salary = salary

    def display(self):
        print(f'ID:{self.id} your salary is {self.salary}')

    @classmethod
    def classmethod(cls):
        print(cls.companyname)
        print(Employee.companyname)
        
        
obj = Employee(1,100000)
obj.display()
obj.classmethod()











