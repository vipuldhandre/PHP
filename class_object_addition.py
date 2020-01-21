class Test:

    def __init__(self,a):
        self.a = a
        

    def __str__(self):
        print("Addition of objects is {}".format(a))


obj1 = Test(1)
obj2 = Test(2)
print(obj1+obj2)
