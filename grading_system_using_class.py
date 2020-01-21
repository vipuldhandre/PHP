##class Grade:
##    def __init__(self,rn,name,marks):
##        self.rn = rn
##        self.name = name
##        self.marks = marks
##
##    def display(self):
##        print(f' Roll No:{self.rn},Name:{self.name} and marks:{self.marks}')
##
##    def grade(self):
##        if self.marks >= 60:
##            print(f'Congratzz! {self.name} you got A grade.')
##        elif self.marks >= 50:
##            print(f'Congratzz! {self.name} you got B grade.')
##        elif self.marks >=40:
##            print(f'Congratzz! {self.name} you got C grade.')
##        else:
##            print(f'Sorry! {self.name} you failed in the exam.')
##
##obj = Grade(1,"Vipul",100)
##obj.display()
##obj.grade()
##
class Grade:
    def __init__(self,rn,name,marks):
        self.rn = rn
        self.name = name
        self.marks = marks

    def display(self):
        print(f'Roll No:{self.rn},Name:{self.name} and marks:{self.marks}')

    def grade(self):
        if self.marks >= 60:
            print(f'Congratzz! {self.name} you got A grade.')
        elif self.marks >= 50:
            print(f'Congratzz! {self.name} you got B grade.')
        elif self.marks >=40:
            print(f'Congratzz! {self.name} you got C grade.')
        else:
            print(f'Sorry! {self.name} you failed in the exam.')

n = int(input("Enter some number:"))
for i in range(n):
    rn = int(input("Enter Your Roll No.:"))
    name = input("Enter Your Name.:")
    marks = float(input("Enter Your Marks:"))
    obj = Grade(rn,name,marks)
    Grade.display(obj)#obj.display()
    obj.grade()
    




