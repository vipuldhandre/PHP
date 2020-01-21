##x,y = 1,1
##def f():
##    global x
##    y = 0
##    for i in (10,20,30):
##        x +=1
##        y +=1
##f()
##print(x,y)
        
##class C(Exception):
##    pass
##b = 1000
##try:
##    b/=b
##    raise C()
##
##except C:
##    print('exception c')
##
##else:
##    print('division')
##try:
##    b= b/5
##except Exception as e:
##    print('inside')
##else:
##    print('division by')

##class UserMainCode(object):
##
##    @classmethod
##    def reverse(cls,input1):
##        start = 0
##        end = len(input1)-1
##        while start < end:
##            input1[start],input1[end] = input1[end],input1[start]
##            start +=1
##            end -=1
##        print(input1)
##
##input1=[2,5,6,0,1]
##
##UserMainCode.reverse(input1)              
            
class UserMainCode(object):
    
    @classmethod
    def historyDocuments(cls,input1):
        str2 = ""
        
        uniqueDates = set()

        for i in range(len(input1)):
            if input1.isdigit():
                str2 += input1[i]

                
            if input1[i] == '-':
                str2 = ""

            if len(str2) == 4:
                uniqueDates.add(str2)
                str2 = ""
        print(len(uniqueDates))

input1 =
"UN was established on 24-10-1945. India got freedom on 15-08-1947." 
UserMainCode.historyDocuments(input1)
