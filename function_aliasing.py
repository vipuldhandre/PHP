##def fun(name):
##    print(name)
##
##fun1 = fun
##
##fun('Vipul')
##fun1('Vipul')
##print(id(fun))
##print(id(fun1))

def fun(name):
    print(name)

fun1 = fun

fun('Vipul')
fun1('Vipul')
print(id(fun))
print(id(fun1))

del fun
fun1('Vipul')
fun('Vipul')
