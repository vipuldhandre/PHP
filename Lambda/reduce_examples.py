from functools import reduce
import time
##li = [1,2,3,4,5,6,7,8,9,10]
##sum = reduce(lambda n,m:n+m,li)
##print(sum)
##
##li2 = [1,2,3,4,5,6,7,8,9,10]
##mul = reduce(lambda n,m:n*m,li2)
##print(mul)

##add = reduce(lambda n,m:n+m,range(1,100))
##print(add)


t1 = time.time()
print(t1)
mul = reduce(lambda n,m:n+m,range(1,100))
print(mul)
t2 = time.time()
print(t2)

