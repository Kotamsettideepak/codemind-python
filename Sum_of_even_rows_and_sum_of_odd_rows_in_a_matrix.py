a,b=map(int,input().split())
l=[]
for i in range(a):
    le=list(input().split())
    le=[eval(i) for i in le]
    l.append(le)
er=[]
ol=[]
for i in range(a):
    for j in range(b):
        if (i+1)%2==0:
            er.append(l[i][j])
        else :
            ol.append(l[i][j])
print(sum(ol),end=' ')
print(sum(er))