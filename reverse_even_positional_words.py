a=input()
a=list(a.split())
r=[]
for i in range(len(a)):
    if i%2==0:
        a[i]=list(a[i])
        a[i].reverse()
        a[i]=''.join(a[i])
print(*a)