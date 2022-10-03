a,b=map(int,input().split())
l=[]
for i in range(a):
    le=list(input().split())
    le=[eval(i) for i in le]
    l.append(le)
sm=0
for i in range(b):
    for j in range(a):
        sm=sm+l[j][i]
    print(sm,end=' ')
    sm=0