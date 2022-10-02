a,b=map(int,input().split())
l=[]
for i in range(0,a):
    le=list(input().split())
    le=[eval(i) for i in le]
    l.append(le)
sm1=0
for i in range(0,a):
    sm1=sm1+l[i][0]
sm2=0
for i in range(1,b):
    sm2=sm2+l[0][i]
sm3=0
for i in range(0,a-1):
    sm3=sm3+l[i+1][b-1]
sm4=0
for i in range(0,b-2):
    sm4=sm4+l[a-1][i+1]
print(sm1+sm2+sm3+sm4)