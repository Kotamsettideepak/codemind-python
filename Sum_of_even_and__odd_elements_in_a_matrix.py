a,b=map(int,input().split())
l=[]
for i in range(a):
    le=list(input().split())
    le=[eval(i) for i in le]
    l.append(le)
le=[]
lo=[]
for i in range(a):
    for j in range(b):
        if l[i][j]%2==0:
              le.append(l[i][j])
        else :
            lo.append(l[i][j])
print(sum(le),end=' ')
print(sum(lo))