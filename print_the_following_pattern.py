a=int(input())
l=[]
r=[]
for i in range(a):
    for j in range(i+1):
        r.append(chr(65+i))
    b=list(r)
    l.append(b)
    r.clear()
l.reverse()
for i in l:
    i=list(i)
    for j in i:
        print(j,end=' ')
    print()