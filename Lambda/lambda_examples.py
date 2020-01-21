from functools import reduce
li = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda n:n%2==0,li))

square = list(map(lambda n:n**2,li))

addition = reduce(lambda n,m:n*m,li)
              
print(even)
print(square)
print(addition)

