a=int(input())
l=list(input().split())
l=[eval(i)for i in l]
b=int(input())
if b in l :
    print("True")
else :
    print("False")