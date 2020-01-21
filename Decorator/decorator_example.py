def decor(func):
    def inner(name):
        if name == "Vipul":
            print("Hello, Vipul GM!")
        else:
            func(name)
    return inner

@decor
def wish(name):
    print("Hello",name , "GM!")

wish('Vikash')
wish("Vipul")
            
