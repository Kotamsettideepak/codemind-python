a=int(input())
l=list(input().split())
l=[eval(i) for i in l]
sm=0
for i in range(a):
    l[i]=str(l[i])
    l[i]=list(l[i])
    l[i]=[eval(j) for j in l[i]]
    sm=sm+sum(l[i])
print(sm)