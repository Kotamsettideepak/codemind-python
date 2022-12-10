a=int(input())
l=[]
for i in range(a):
    nl=list(map(int,input().split()))
    l.append(nl)
f=[]
d=[]
for r in range(a):
    for c in range(a):
        if r==c:
            d.append(r)
            d.append(c)
            c=list(d)
            f.append(c)
            d.clear()
c=a-1
for r in range(a):
    d.append(r)
    d.append(c)
    m=list(d)
    if m not in f:
        f.append(m)
    d.clear()
    c=c-1
sm=0
for i in f:
    sm=sm+l[i[0]][i[1]]
print(sm)