def timer(num):
    print("Start Timer")
    while num > 0:
        yield num
        num -= 1

value = timer(10)
for i in value:
    print(i)
