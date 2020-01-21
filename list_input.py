##sum = 0
##li = eval(input("Enter some list:"))
##for i in li:
##    sum = sum + i
##print(f'Sum of all elements of list is:{sum}')

#Que: WAP to print first N numbers.
##count = int(input("Enter a number:"))
##number = 0
##while(number<count):
##    number = number + 1
##    print(number,end = " ")
    
##number = int(input("Enter a number:"))
##for i in range(1,number+1):
##    print(i)

#Que: WAP to print first N numbers in reverse order.
##number = int(input("Enter a number:"))
##for i in range(number,0,-1):
##    print(i)

# Que: WAP to print first N odd numbers?
##number = int(input("Enter a number:"))
##for i in range(1,number+1):
##    if (i%2!=0):
##        print(i)

##Que: WAP to accept the list and print only integer from that list?
##(With eval and without eval)(For Heterogeneous data)
#(With eval)
##li = []
##number = eval(input("Enter the elements of list:"))
##for i in number:
##    if (type(i) == int):
##        li.append(i)
##print("List with only integer elements:",li)

#(Without eval)
##li = []
##number = input("Enter the elements of list:")
##new_number = int(number) 
##for i in new_number:
##    if (type(i) == int):
##        li.append(i)
##print("List with only integer elements:",li)

### WAP to accept a numbers and accept those elements and if the elements is not integer then add it to the list and print the list?
##li = []
##list_with_non_integer = []
##count = int(input("How many elements:"))
##i = 0
##while(i<count):
##    number = eval(input("Enter the element:"))
##    li.append(number)
##    i +=1
##print("Entered elements are:",li)
##for j in li:
##    if(type(j) != int):
##        list_with_non_integer.append(j)
##print("List with non-integer elements:",list_with_non_integer)
        
    

##d = {}
##l1 = [1,2]
##l2 = ['a','b']
##for x,y in zip(l1,l2):
##    d[x]=y
##print(d)

# WAP to accept the list from user and reverse that list after that print the some of list elements which is at odd index?

