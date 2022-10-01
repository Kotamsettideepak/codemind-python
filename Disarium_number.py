a=int(input())
b=a
a=str(a)
l=list(a)
le=len(l)
l=[eval(i)for i in l]
sm=0
for i in range(0,le):
    c=l[i]**(i+1)
    sm=sm+c
if sm==b:
    print("True")
else :
    print("False")