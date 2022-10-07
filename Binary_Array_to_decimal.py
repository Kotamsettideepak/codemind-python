a=int(input())
l=list(input().split())
l=[eval(i) for i in l]
j=0
sm=0
for i in range(-1,-(len(l)+1),-1):
    sm=sm+(l[i]*(2**j))
    j+=1
print(sm)