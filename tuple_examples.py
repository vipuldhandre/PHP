#tuple :-

"""
t = tuple("Vipul")
print(t)
"""

#output :- ('V', 'i', 'p', 'u', 'l')

"""
t = tuple(range(25))
print(t)
"""

#output:-(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)

# +,&,* operator is applicable on tuple.

"""
t1=(1,2,3)
print(id(t1))
t2=(4,5,6)
print(id(t2))
t1=t1*3
print(t1)
print(id(t1))
"""

"""
         0       1
t1 = ((1,2,3),(4,5,6))
       0 1 2   0 1 2
"""

"""
t = ((1,2,3),(4,5,6))
a , b = t
a1,a2,a3= a
b1,b2,b3= b
print(a)
print(a1)
print(a2)
print(a3)
print(b)
print(b1)
print(b2)
print(b3)
"""

#WAP to sort tuple in reverse order.
"""
t1 = (5,4,3,2,1)
t2 = (1,2,3,4,5)
print(t1)
print(t2)
li1 = list(t1)
li1.sort()
li2 = list(t2)
li2.sort(reverse=True)
##print(li)
t1 = tuple(li1)
t2 = tuple(li2)
print(t1)
print(t2)
"""

#count,index,len,slicing
#
