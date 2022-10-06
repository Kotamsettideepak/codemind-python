a=int(input())
c=0
for i in range(1,a+1):
    if a%i==0:
        c+=1
if c !=2:
    print("not prime")
else :
    c=0
    a=str(a)
    l=list(a)
    l.reverse()
    l=''.join(l)
    l=int(l)
for i in range(1,l+1):
    if l%i==0:
        c+=1  
if c==2:
    print("circular prime")
else :
    print("prime but not a circular prime")