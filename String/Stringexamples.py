##s = input("Enter Some String:")
##l = s.split()
##
##l1 = []
##i = len(s) - 1
##
##while i >= 0:
##    l1.append(l[i])
##    i = i-1
##output = ''.join(l1)
##print(output)

##s = input("Enter Some String:")
##l = s.split()
##l1 = []
##i = 0
##while i < len(l):
##    l1.append(l[i][::-1])
##    i = i+1
##output = ' '.join(l1)
##print(output)
    
##s = input("Enter First String:")
##s1 = input("Enter Second String:")
##output = ''
##i,j = 0,0
##while i < len(s) or j < len(s1):
##    if i < len(s):
##        output = output + s[i]
##        i = i + 1
##    if j < len(s1):
##        output = output + s1[j]
##        j = j + 1
##print(output)

s = input("Enter Some String:")
s1 = s2 = output = ''
for x in s:
    if x.isalpha():
        s1 = s1 + x
    else:
        s2 = s2 + x
for x in sorted(s1):
    output = output + x
for x in sorted(s2):
    output = output + x
print("Output:",output)














        











        
