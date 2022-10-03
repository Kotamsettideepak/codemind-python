a,b=map(int,input().split())
l=[]
for i in range(a):
    le=list(input().split())
    le=[eval(i) for i in le]
    l.append(le)
rl=[]
sm=0
for i in range(a):
    for j in range(b):
        sm=sm+l[i][j]
    rl.append(sm)
    sm=0
rl.sort()
print(rl[-1])