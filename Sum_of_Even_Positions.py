a=int(input())
l=list(input().split())
l=[eval(i) for i in l]
r=[]
for i in range(len(l)):
    if i%2==0:
        r.append(l[i])
print(sum(r))