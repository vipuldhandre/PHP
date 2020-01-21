def first(num):
    n = 1
    while n <= num:
        yield n
        n = n + 1

value = first(10)
for x in value:
    print(x)
