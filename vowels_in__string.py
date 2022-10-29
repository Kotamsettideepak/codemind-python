a=input()
a=list(a.split())
v=['a','e','i','o','u']
l=a[0]
r=[]
f=[]
for i in range(1,len(a)):
    l=l+a[i]
for i in range(len(l)):
    for j in range(len(v)):
        if l[i]==v[j] or l[i]==v[j].capitalize():
            r.append(l[i])
for i in range(len(r)):
    if r[i] not in f:
        f.append(r[i])
for i in range(len(f)):
    print(f[i],end=' ')