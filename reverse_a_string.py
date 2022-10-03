a=input()
a=list(a.split())
a.reverse()
for i in range(len(a)):
    b=list(a[i])
    b.reverse()
    b=''.join(b)
    print(b,end=' ')