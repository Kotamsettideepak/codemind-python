a,b=map(int,input().split())
l=list(input().split())
m=0
for i in range(a):
    c=int(l[i])
    if c<0:
        c=-(c)
    c=str(c)
    c=list(c)
    if len(c)==b:
        m+=1
print(m)