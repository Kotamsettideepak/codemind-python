a=int(input())
l=list(map(int,input().split()))
r=[]
check=[]
count=0
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]==l[j]:
            count+=1
    if count==l[i]:
        if l[i] not in r :
            r.append(l[i])
    count=0
print(len(r))