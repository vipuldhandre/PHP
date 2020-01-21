##break statement: The main purpose of break statement is to break a loop.
"""
for i in range(10):
    if i==7:
        break
    else:
        print(i)
"""
##WAP to print even number upto'N' with break statements.
"""
n = int(input("Enter the value:"))
i=1
while True:
    if i==n:
        break
    else:
        if i%2==0:
            print("Even:",i)
        i+=1

"""
#WAP that input a number and convert it into binary number of list without using any inbulit
#function of python.
"""
n = int(input("Enter the number:"))
li = []
for i in range(n+1):
    x = n%2
    li.append(x)
    n = n//2
    if n == 0:
        break
end = len(li) - 1
start = 0
while (start < end):
    li[start],li[end] = li[end],li[start]
    end -= 1
    start += 1
print(li)
"""
            
    
#Given a list of integers and a number with it's position.Your program should insert
#the number in that specified position of list with other elements preceding it should
#shift to right by one place.
#e.g input [1,2,3,4,5]
# position - 4,number - 9
#output [1,2,3,4,9,5]
#if position is not present then it should return the list as it is.

    
    
