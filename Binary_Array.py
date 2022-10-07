a=int(input())
l=list(input().split())
l=[eval(i) for i in l]
c=0
for i in range(a):
    if l[i]==0 or l[i]==1:
        c+=1
if c==a:
    print("True")
else :
    print("False")