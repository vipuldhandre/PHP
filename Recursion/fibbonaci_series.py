def rec_fibb(x):
    if x <= 1 :
        return x
    else:
        return (rec_fibb(x-1)+rec_fibb(x-2))

num = int(input("Enter the number:"))

if num <= 0:
    print("Enter a positive integer")
else:
    for i in range(num):
        print(rec_fibb(i))
