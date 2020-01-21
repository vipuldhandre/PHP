#for_else,while_else:
# when break run then else statements won't run. And, when break unable to run then else will run.
"""
l=[100,200,10,20,555,350,400,650,800]
for x in l:
    if x>500:
        break
    else:
        print(f'{x} is proceed')
else:
    print("All items are proceed,congo!")

"""
"""
l=[100,200,10,20,555,350,400,650,800]
for x in l:
    if x>1000:
        break
    else:
        print(f'{x} is proceed')
else:
    print("All items are proceed,congo!")
"""

for i in range(5):
    for j in range(1,5-i):
        print(" "*j,end=" ")
