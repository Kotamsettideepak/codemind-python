a,b=map(int,input().split())
la=list(input().split())
lb=list(input().split())
la=set(la)
lb=set(lb)
la=list(la)
lb=list(lb)
la=[eval(i) for i in la]
lb=[eval(i) for i in lb]
c=0
for i in range(0,len(la)):
    if la[i] in lb :
        c+=1
print(c)