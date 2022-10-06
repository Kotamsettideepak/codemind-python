a=int(input())
l=[]
for i in range(1,a+1):
    if a%i==0:
        l.append(i)
c=0
r=0
for i in range(len(l)):
    b=l[i]
    for j in range(1,b+1):
        if b%j==0:
            c+=1
    if c!=2:
        r+=1
    c=0
print(r)