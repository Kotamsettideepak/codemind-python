a=int(input())
l=list(input().split())
l=[eval(i) for i in l]
ol=[]
el=[]
for i in range(a):
    if l[i]%2==0:
        el.append(l[i])
    else :
        ol.append(l[i])
r=ol+el
for i in range(a):
    print(r[i],end=' ')