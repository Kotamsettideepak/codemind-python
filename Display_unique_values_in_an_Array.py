a=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    c=0
    for j in l:
        if i==j:
            c+=1
    if c==1:
        r.append(i)
if len(r)==0:
    print(-1)
else :
    print(*r)