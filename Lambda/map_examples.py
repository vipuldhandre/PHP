li = [1,2,3,4,5]
l1 = list(map(lambda n:n*n,li))
print(l1)

li2 = [1,2,3,4,5]
li3 = [5,4,3,2,1]
l1 = list(map(lambda n,m:n*m,li2,li3))
print(l1)
