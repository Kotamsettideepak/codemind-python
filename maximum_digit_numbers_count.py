a=int(input())
l=list(input().split())
m=0
for i in range(a):
    b=list(l[i])
    if len(b)>m:
        m=len(b)
c=[]
for i in range(a):
    b=list(l[i])
    if len(b)==m:
        b=''.join(b)
        b=int(b)
        c.append(b)
for i in range(len(c)):
    print(c[i],end=' ')
    