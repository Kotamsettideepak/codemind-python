a=int(input())
l=list(input().split())
l=[eval(i) for i in l]
sm=0
for i in range(len(l)):
    sm=sm+l[i]
print(sm)