n=input()
n=n.split()
h=0
r=[]
d=[]
for i in n:
    i=list(i)
    i=len(i)
    if i>h:
        h=i
for i in range(1,h+1):
    for j in n:
        j=list(j)
        x=len(j)
        if x ==i:
            j=''.join(j)
            d.append(j)
    d.sort()
    c=list(d)
    for m in c:
        r.append(m)
    d.clear()
print(*r)