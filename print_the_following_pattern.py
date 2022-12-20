a=int(input())
l=[['x']*a]*a
r=[]
for i in range(a):
    b=list(l[i])
    b[i]=0
    c=list(b)
    r.append(c)
for i in r:
    a=list(i)
    for j in range(len(a)):
        print(a[j],end='')
    print()