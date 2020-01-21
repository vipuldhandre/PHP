class Phone:
    def __init__(self,brand,modelname,price):
        self.brand = brand
        self.modelname = modelname
        self.__price = price

    def make_a_call(self,phone_no):
        print(f'Making a phone call on {phone_no}.....')

obj = Phone("Nokia","7.1",12000)
print(obj.__dict__)
print(obj._Phone__price)
obj._Phone__price = 19000
print(obj._Phone__price)
obj.make_a_call(7744930919)

