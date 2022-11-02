a=int(input())
l=list(map(int,input().split()))
sm=0
for i in l:
    if i % 2==0:
        break
    else :
        sm =sm + i
print(sm)