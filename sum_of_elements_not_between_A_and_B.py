a=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
sm=0
for i in l:
    if i<b or i>c:
        sm=sm+i
print(sm)