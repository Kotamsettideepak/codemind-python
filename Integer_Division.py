a=int(input())
if a>=0:
    print(a//10)
else :
    a=-(a)
    c=a%10
    if c==0:
        print(-(a//10))
    else:
        c=10-c
        a=a+c
        print(-(a//10))