a=int(input())
l=list(input().split())
l=[eval(i) for i in l]
a=sum(l)
avg=a/len(l)
avg=int(avg)
if avg in l :
    print("True")
else :
    print("False")