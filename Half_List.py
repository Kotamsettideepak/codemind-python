a=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(-1,-((len(l)//2)+1),-1):
    r.append(l[i])
for i in range(len(l)//2):
    r.append(l[i])
print(*r)