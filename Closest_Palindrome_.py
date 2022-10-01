a=int(input())
l=[]
for i in range(0,a):
    i=str(i)
    b=list(i)
    c=list(i)
    b.reverse()
    if c==b:
        c=''.join(c)
        c=int(c)
        l.append(c)
mi = a-l[-1]
mx=a+mi
mx=str(mx)
lmx=list(mx)
nlmx=list(mx)
lmx.reverse()
if lmx==nlmx :
    lmx=''.join(lmx)
    lmx=int(lmx)
    print( l[-1] ,end=' ')
    print(lmx)
else :
    print(l[-1])