def square():
    num = 1
    while num <= 10:
        yield num**2
        num += 1

for i in square():
    print(i)
    
