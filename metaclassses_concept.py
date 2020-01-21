##class ClassName:
##    pass
##c = ClassName()
##print(c)
##print(type(c))
##print(type(ClassName))
##print(type(type))
##print(type(type))
##print(type(object))

##class ClassName(object):
##    pass
##obj = ClassName()
##print(obj)
##ClassName = type('ClassName',(),{})
##print(ClassName)


##class ClassName(object):
##    party = 'True'
##
##print(ClassName.party)
##
##ClassName = type('ClassName',(object,),{'party':True})
##print(ClassName.party)
##    

##class ClassName(object):
##    name = "Vipul"
##    rollno = 10
##print(ClassName.name)
##print(ClassName.rollno)
##
##ClassName = type('ClassName',(object,),{'nm':'Vipul','rn':10})
##print(ClassName.nm)
##print(ClassName.rn)                

##class Car(object):
##
##    def wheel(self):
##        return 4
##obj = Car()
##print(obj.wheel())
##
##def wheel(self):
##    return 10
##Truck = type('Truck',(object,),{'wheel':wheel})
##obj = Truck()
##print(obj.wheel())

class Parrot(object):

    name = "Parrot"
    age = 2

    def fly(self):
        return Parrot.name,Parrot.age
        
obj = Parrot()
print(obj.fly())
print("*"*50)

name = "Fish"
age = 1

def swim(self):
    return Fish.name,Fish.age

Fish = type('Fish',(object,),{'swim':swim,'name':name,'age':age})
obj = Fish()
print(obj.swim())


