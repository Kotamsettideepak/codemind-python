a=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
sm=0
r=[]
for i in l:
    if i<b or i>c:
        r.append(i)
if len(r)==0:
    print(-1)
else :
    print(*r)