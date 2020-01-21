class Test:

    count = 0

    def __init__(self):
        Test.c
        ount = Test.count + 1

    @classmethod
    def getnoofobject(cls):
        print("Number of objects created by user:",Test.count)

obj = Test()
obj.getnoofobject()
obj1 = Test()
obj1.getnoofobject()
obj2 = Test()
obj2.getnoofobject()
