a=int(input())
l=list(map(int,input().split()))
k=int(input())
r=[]
count=0
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]==l[j]:
            count+=1
    if count==k:
        if l[i] not in r :
            r.append(l[i])
    count=0
if len(r)==0:
    print('-1')
else :
    for i in r:
        print(i,end=' ')