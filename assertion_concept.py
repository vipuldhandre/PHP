##def sq(x):
##    
##    return x**x
##
##print(sq(0))
##print(sq(1))
##print(sq(2))
##print(sq(3))
##print(sq(4))
##print(sq(5))
##print(sq(6))
##print(sq(7))
##print(sq(8))
##print(sq(9))
##print(sq(10))

##def sq(x):
##    return x**x
##
##assert sq(2) == 4,'square of 2 is 4'
##assert sq(3) == 9,'square of 3 is 9'
##assert sq(4) == 16,'square of 4 is 16'
##assert sq(5) == 25,'square of 5 is 25'
##assert sq(6) == 36,'square of 6 is 36'
##assert sq(7) == 49,'square of 7 is 49'
##assert sq(8) == 64,'square of 8 is 64'
##assert sq(9) == 81,'square of 9 is 81'

##def sq(x):
##    return x**x
##
##assert sq(4) == 16,'Expected output.'
##print(sq(4))

##age = int(input("Enter your age:"))
##print("game is loading.....")
##
##if age:
##    assert age >= 18,'You can not play game'
##    print("You can play game")

##def m1(x):
##    assert x > 0,'Negative age'
##    print(f'My current age is:{x}')
##
##m1(1)
##m1(-1)

def avg(l):
    assert len(l) != 0,'Enter some element in list'
    c = sum(l)/len(l)
    return c
print(avg([1,2,3]))
print(avg([]))
