##string = "Hello Vipul"
##a = string.upper()
##print(a)
##a = string.lower()
##print(a)
##a = string.capitalize()
##print(a)
##a = string.split()
##print(a)
##a = string.split('l')
##print(a)

##li = [[1,2,3],[4,5,6],[7,8,9]]
##x = [i[2] for i in li]
##print(x)

##s = "Global Variable"
##
##def function():
##    
##    
##    print(locals())
##    print(globals())
##
##
##print(function())
##print(s)


##def hello(name="Vipul"):
##    return "hello " + name
##print(hello())
##
##mynewgreet = hello
##
##print(mynewgreet())


##def hello(name="Vips"):
##    print("Hello() function is run!")
##
##    def greet():
##        return "This is greet() fucntion"
##
##    def welcome():
##        return "This is welcome() function"
##
##    if name == "Vips":
##        return greet
##    else:
##        return welcome
##
##x = hello()
##print(x())


##def hello():
##    return "Hi Vipul"
##
##def other(function):
##    print("Hi")
##    print(function())
##
##other(hello)

def new_decorator(function):

    def wrap_function():
        print("Code before executing a function")
        function()
        print("function() has been called")

    return wrap_function

@new_decorator
def function_needs_decorators():
    print("This fucntion needs a decorators")

function_needs_decorators()



        











