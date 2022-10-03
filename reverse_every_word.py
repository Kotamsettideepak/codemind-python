a=input()
a=list(a.split())
for i in range(len(a)):
    a[i]=list(a[i])
    a[i].reverse()
    a[i]=''.join(a[i])
    print(a[i],end=' ')