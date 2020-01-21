def fact(x):
    """This is the recursive function to
        find factorial of a number."""

    if x == 1:
        return 1
    else:
        return (x*fact(x-1))

num = int(input("Enter a number:"))
print("Factorial of {} is {}".format(num,fact(num)))
        
