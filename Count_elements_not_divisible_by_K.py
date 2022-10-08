a,b=map(int,input().split())
l=list(input().split())
l=[eval(i) for i in l]
c=0
for i in range(a):
    if l[i]%b!=0:
        c+=1
print(c)