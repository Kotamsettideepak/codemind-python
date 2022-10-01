a=int(input())
count=0
for i in range(a+1,a*a*a):
    x=i
    i=str(i)
    l=list(i)
    b=list(l)
    l.reverse()
    if b==l :
        for j in range(1,x+1):
            if x%j==0:
                count+=1
        if count==2:
            print(x)
            break
        count=0