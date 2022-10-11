a=int(input())
l=list(input().split())
m=0
for i in range(a):
    b=list(l[i])
    if len(b)>m:
        m=len(b)
c=0
for i in range(a):
    b=list(l[i])
    if len(b)==m:
        c+=1
print(c)