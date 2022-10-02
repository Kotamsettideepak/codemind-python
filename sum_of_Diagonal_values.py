a,b=map(int,input().split())
if b%2==0:  
    l=[]
    for i in range(0,a):
        le=list(input().split())
        le=[eval(i)for i in le]
        l.append(le)
    sm1=0
    for i in range(0,a):
        for j in range(0,b):
            if i==j :
                sm1=sm1+l[i][j]
    sm2=0
    for i in range(a):
        sm2=sm2+l[i][b-1]
        b=b-1
    print(sm1+sm2)
else :
    l=[]
    for i in range(0,a):
        le=list(input().split())
        le=[eval(i)for i in le]
        l.append(le)
    sm1=0
    for i in range(0,a):
        for j in range(0,b):
            if i==j :
                sm1=sm1+l[i][j]
    sm2=0
    for i in range(0,a):
        if i!=(b-1):
            sm2=sm2+l[i][b-1]
        else:
            pass
        b-=1
    print(sm1+sm2)