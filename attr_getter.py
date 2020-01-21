from operator import attrgetter

class Employee:
    emp_id = 0
    emp_name = ""
    emp_designation = ""
    emp_level = ""
    emp_address = ""

    def __init__(self,id,name,designation,level,address):
        self.id = id
        self.name = name
        self.designation = designation
        self.level = level
        self.address = address

    def __str__(self):
        return("Id:{},Name:{},Designation:{},Level:{},Address:{}".format(self.id,self.name,self.designation,self.level,self.address))

emp_list = []

num = int(input("Enter the number of Employees:"))
for i in range(num):
    id = int(input("Enter Employee Id:"))
    name = str(input("Enter Employee Name:"))
    designation = str(input("Enter Employee Designation:"))
    level = str(input("Enter Employee Level:"))
    address = str(input("Enter Employee Address:"))
    e = Employee(id,name,designation,level,address)
    emp_list.append(e)
print("*********** Employee List Before Sorting is ***********")
for i in emp_list:
    print(i)


while True:
    print("1.Sort by Id \n2.Sort by Name \n3.Sort by Designation \n4.Sort by Level \n5.Sort by Address")
    choice = int(input("Enter your Choice:"))    
    if choice == 1:
        print("Sort by Id")
        new_emp_list = sorted(emp_list,key = attrgetter("id"))
        for emp in new_emp_list:
            print(emp)

    elif choice == 2:
        print("Sort by Name")
        new_emp_list = sorted(emp_list,key = attrgetter("name"))
        for emp in new_emp_list:
            print(emp)

    elif choice == 3:
        print("Sort by Designation")
        new_emp_list = sorted(emp_list,key = attrgetter("designation"))
        for emp in new_emp_list:
            print(emp)

    elif choice == 4:
        print("Sort by Address")
        new_emp_list = sorted(emp_list,key = attrgetter("address"))
        for emp in new_emp_list:
            print(emp)

    elif choice == 5:
        break
    
            
                              
        
    
