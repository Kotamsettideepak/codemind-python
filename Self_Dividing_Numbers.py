a=int(input())
b=int(input())
couont=0
for i in range(a,b+1):
    c=i
    i=str(i)
    i=list(i)
    i=[eval(m) for m in i]
    if 0 in i:
        continue
    for j in range(len(i)):
        if c%i[j]==0:
            couont+=1
    if couont==len(i):
        print(c,end=' ')
    couont=0