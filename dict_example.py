# Que: {'1':4,'2':3,'3':6,'4':7}
# Output : ['1','1','1','1','2','2','2','3','3','3','3','3','3','4','4','4','4','4','4','4']

##di = {'1':4,'2':3,'3':6,'4':7}
##li = []
##li_new = []
##for x,y in di.items():
##    li.append(x*y)
##for i in li:
##    for j in i:
##        li_new.append(j)
##print(li_new)

##di = {'1':4,'2':3,'3':6,'4':7}
##li = []
##
##for x,y in di.items():
##    for l in x*y:
##        for i in l:
##            for j in i:
##                li.append(j)
##print(li)

#Que: input = [1,1,1,2,2,2,2,3,3]
#Ans: output = {'1':3,'2':4,'3':2}

li = [1,1,1,2,2,2,2,3,3]
di = {}
for x in li:
    di[x] = di.get(x,0)+1

print(di)
