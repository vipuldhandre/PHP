def sum_of_numbers(x):
    if x <= 0:
        return x
    else:
        return (x+sum_of_numbers(x-1))

num = int(input("Enter a number:"))
if num < 0:
    print("Enter positive integer")
else:
    print("Sum of {} numbers is {}".format(num,sum_of_numbers(num)))
    
