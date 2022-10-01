a=int(input())
l=[]
for i in range(1,a):
    if a%i==0:
        l.append(i)
sm=sum(l)
if sm>a:
    print("True")
else :
    print("False")