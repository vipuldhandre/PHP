##s = "Learning python is very easy!!!"
##print("Forward direwction")
##for i in s:
##    print(i,end="")
##print()
##print("Backward Direction")
##for i in s[::-1]:
##    print(i,end="")

##i= 0
##n = len(s)
##print("Forward Direction")
##while i < n:
##    print(s[i],end="")
##    i+=1
##print()
##print("Backward Direction")
##
##i=-1
##while i>= -n:
##    print(s[i],end="")
##    i-=1
##    

##s =input("Enter a string:")
##subs = input("Enter a substring:")
##if subs in s:
##    print("yes")
##else:
##    print("no")

##s = input("Enter the string:")
##l=s.lstrip()
##b = s.strip()
##
##print(s)
##print(l)
##print(b)

##s =input("Enter a string:")
##sub = input("Enter a substring:")
##flag = False
##pos = -1
##n = len(s)
##while True:
##    pos = s.find(sub,pos+1,n)
##    if pos == -1:
##        break
##    print("{} find at position {}".format(sub,pos))
##    flag = True
##if flag == False:
##    print("Not Found")

##s = input("Enter a string:")
##print(s.count('a'))
##print(s.count('ab'))

s = input("ENter a string:")
a = s.rstrip(".")
l= a.split(" ")
print(l)
for i in l:
    print(i)

















