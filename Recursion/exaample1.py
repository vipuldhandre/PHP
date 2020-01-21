import sys

sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())

i=0
def fun1():
    global i
    i+=1
    print("Hi",i)
    fun1()

fun1()
