##import time
##def count(num):
##    print("Start Countdown")
##    while num>0:
##        yield num
##
##a = count(50)
##for x in a:
##    print(x)
##    time.sleep(1)
        
##import time
##def count(num):
##    print("Start Countdown")
##    while num>0:
##        yield num
##        num = num - 1
##
##a = count(50)
##for x in a:
##    print(x)
##    time.sleep(1)
        
import time
def count(num):
    print("Start Countdown")
    for num in range(num,1,-1):
        yield num

a = count(50)
for x in a:
    print(x)
    time.sleep(1)
        
