a=int(input())
l=list(input().split())
l=[eval(i) for i in l]
sm=sum(l)
avg=sm//a
c=0
for i in range(a):
    if l[i]>=avg:
        c+=1
print(c)