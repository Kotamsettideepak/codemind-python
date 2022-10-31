a=int(input())
l=list(map(int,input().split()))
ec=0
for i in range(len(l)):
    if l[i]==0:
        ec+=1
    elif l[i]%2==0:
        ec+=1
check=0
for i in range(len(l)):
    if i==0 and l[i]==0:
        check+=1
    elif i %2==0 and l[i]%2==0:
        check+=1
if check ==ec:
    print(True)
else :
    print(False)