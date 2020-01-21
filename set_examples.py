#Set :
#empty set
#s = set()
#type(s1)
# Unordered,mutable,heterogeneous,insertion order is not preserved.

#WAP to print 25 elements in a set.
"""
x = [x for x in range(25)]
s = set(x)
print(s)
"""
# set doesn't mutable data.
# s = {1,2,[4,5,6],7,8}
# error: Unhashable type s

"""
s = set()
s.add(2)
s.add("vipul")
print(s)
s.update([4,5,'vips',80])
print(s)
"""

# Update method works on only iterable data.
# How to copy a set.
# By using copy method

"""
s1 = {1,2,3,4,5,6}
s2 = set()
s2=s1.copy()
print(s2)
"""

#Bitwise Operator:
"""
a = set("Vipul")
b = set("Dhandre")
print(a-b) # letters in a but not from b.
print(a|b) # letters in a or b or both.
print(a&b) # letters in both a and b.
print(a^b) # letters in a or b. But, not both.
"""
# Indexing and slicing is not applicable on a set.
# By using for loop we can access the elements of set.

"""
s = {1,2,3,4,5}
for i in s:
    print(i)
"""

#Tuple Comprehension is not possible in python.
#Internally,tuple comprehension is nothing but generator concept.

# Set Comprehension.
"""
s = {x for x in range(100) if x%2==0}
print(type(s))
print(s)
"""

# How to remove elements of set.
#remove : to remove particular element.
# syntax : s.remove(element)
#pop : It remove by default first element.
#discard: it remove given element.
#syntax: s.discard(value)
#clear: it delete total set.

"""
s = {1,2,3,4,5,6}
s.remove(2)
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.discard(5)
print(s)
s.clear()
print(s)
"""

# Set inside set is not allowed.
"""
s = {1,2,3,4,5,6}

print(min(s))

print(max(s))
"""
#sorting of set

s = {10001,200,1000000,13335,3173}
print(sorted(s))
s1 = set
print(sorted(s,reverse = True))
