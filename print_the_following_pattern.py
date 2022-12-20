a=int(input())
l=[[0]*a]*a
if a%2 != 0:
    for i in range(a//2):
        b=list(l[i])
        b[-i-1]='x'
        b[i]='x'
        c=list(b)
        l[i]=c
        b.clear()
    l[a//2][a//2]='x'
    for i in range(a//2):
        l[-i-1]=l[i]
    for i in range(len(l)):
        b=list(l[i])
        for j in range(len(b)):
            print(b[j],end='')
        print()
else :
    for i in range((a//2)-1):
        b=list(l[i])
        b[-i-1]='x'
        b[i]='x'
        c=list(b)
        l[i]=c
        b.clear()   
    l[a//2][a//2]='x'
    l[a//2][(a//2)-1]='x'
    l[(a//2)-1][a//2]='x'
    l[(a//2)-1][(a//2)-1]='x'
    for i in range(a//2):
        l[-i-1]=l[i]
    for i in l:
        a=list(i)
        for j in range(len(a)):
            print(a[j],end='')
        print()