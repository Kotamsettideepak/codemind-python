a=input()
a=list(a.split())
l=a[0]
for i in range(1,len(a)):
    l=l+a[i]
vl=['a','e','i','o','u']
r=[]
l=set(l)
l=list(l)
for i in range(len(l)):
    if l[i] in vl:
        r.append(l[i])
fr=[]
for i in range(len(vl)):
    if vl[i] not in r:
        fr.append(vl[i])
if len(fr)>0:
    fr.sort()
    for i in fr:
        print(i,end=' ')
else :
    print(0)