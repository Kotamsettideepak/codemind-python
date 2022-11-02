a=input()
a=list(a.split())
l=a[0]
for i in range(1,len(a)):
    l=l+a[i]
l=set(l)
l=list(l)
vl=['a','e','i','o','u']
c1=0
c2=0
for i in range(len(l)):
    if l[i] in vl:
        c1+=1
    for j in range(len(vl)):
        if l[i] in vl[j].capitalize():
            c2+=1
if c1==len(vl) or c2==len(vl):
    print(True)
else :
    print(False)