a=int(input())
l=list(input().split())
l=[eval(i) for i in l]
lo=[]
for i in range(0,a):
    if l[i]%2 !=0:
        lo.append(l[i])
print(lo[-1])