a=input()
a=a.split()
l=[]
for i in a:
    i=list(i)
    l.append(min(i))
    l.append(max(i))
for i in l:
    print(i,end=' ')