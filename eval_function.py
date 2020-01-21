##Que: Why to use eval function?
##1.No need of type casting.
##2.We can solve big and complex expressions very easily by using eval function.
##Note: eval function is always works on string only.

##a=eval(input("enter no.:"))
##print(a)

##a = eval("10.5+10/3*2%3**30//3")
##print(a)

##que: WAP to evaluate user provided input?

a = input("Enter a number:")
number = eval(a)
print(number)
