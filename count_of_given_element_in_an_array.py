a=int(input())
l=list(input().split())
l=[eval(i) for i in l]
b=int(input())
c=0
for i in range(0,a):
    if b==l[i]:
        c+=1
print(c)