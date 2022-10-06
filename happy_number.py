a=int(input())
x=True
while x:
    sm=0
    a=str(a)
    l=list(a)
    l=[eval(i) for i in l]
    le=len(l)
    if le==1:
        if a=='1' or a=='7':
            print("True")
        else:
            print("False")
        x=False
    else :
        for i in range(le):
            sm=l[i]*l[i]+sm
            a=sm