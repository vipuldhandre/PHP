##if statement:
##if condition is true then execute if part.
##username = input("Enter the username:")
##password = input("Enter the password:")
##
##if (username == "vipul_dhandre") and (password == "VipsAmsterdam"):
##    
##    print("Welcome to Instagram")

##if-else statement:
##if condition is true then execute if part.Else,execute else part.
    
##a,b = [int(x) for x in input("Enter 2 numbers to find greatest of 2 numbers:").split(",")]
##
##if (a>b):
##    print("Greater number is:",a)
##else:
##    print("Smaller number is:",b)

##if-elif-elif-else statement
##que: WAP to accept students marks and display 1st class,2nd class,3rd class and fail.

marks = float(input("Enter marks of student:"))
if (marks>=75):
    print("1st class with distinction")
elif (marks>=60) and (marks<75):
    print("1st class")
elif (marks>=45) and (marks<60):
    print("2nd class")
elif (marks>=40) and (marks<45):
    print("3rd class")
else:
    print("Sorry,Better luck.\nTry next time.")



