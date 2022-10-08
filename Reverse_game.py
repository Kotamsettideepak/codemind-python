a=int(input())
l=list(input().split())
l=[eval(i) for i in l]
r=[]
for i in range(a):
    l[i]=str(l[i])
    l[i]=list(l[i])
    l[i].reverse()
    l[i]=''.join(l[i])
    l[i]=int(l[i])
    r.append(l[i])
for i in range(len(r)):
    print(r[i],end=' ')