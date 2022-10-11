a=int(input())
l=list(input().split())
for i in range(a):
    b=int(l[i])
    if b<0:
        b=-(b)
    b=str(b)
    b=list(b)
    print(len(b),end=' ')