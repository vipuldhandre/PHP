def fun():
    yield 'A'
    yield 'B'
    yield 'C'

obj = fun()

print(type(obj))

print(obj.__next__())
print(next(obj))
print(obj.__next__())

