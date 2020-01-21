#Nesting of loop:(loop inside a loop)
#Outer for loop is always going to represent number of rows.
#Inner for loop is always agoing to represent number of columns.
#Note: number of iteration of inner o inner for loop is always depends on inner for loop.
for i in range(3):
    #print(i)
    for j in range(4):
        print(j,end=" ")
    print()
    
