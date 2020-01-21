count = 0
addition = 0
even_add = 0
odd_add = 0
number = int(input("Enter a number:"))
while(number>0):
    rem = number % 10
    count = count + 1
    number = number // 10
print(count)
if (count == 6):
    if(number % 2 == 0):
        even_add = even_add + number
    else:
        odd_add = odd_add + number
print(even_add)
print(odd_add)
    
