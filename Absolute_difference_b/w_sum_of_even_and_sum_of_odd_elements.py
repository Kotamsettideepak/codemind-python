a=int(input())
l=list(input().split())
l=[eval(i) for i in l]
el=[]
ol=[]
for i in range(len(l)):
    if l[i]%2==0:
        el.append(l[i])
    else :
        ol.append(l[i])
r=sum(el)-sum(ol)
if r>0:
    print(r)
else :
    print(-r)