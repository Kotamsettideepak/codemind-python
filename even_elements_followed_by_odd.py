a=int(input())
l=list(input().split())
l=[eval(i) for i in l]
el=[]
ol=[]
for i in range(a):
    if l[i]%2==0:
        el.append(l[i])
    else :
        ol.append(l[i])
r=el+ol
for i in range(len(r)):
    print(r[i],end=' ')