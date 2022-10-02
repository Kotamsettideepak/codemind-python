a=int(input())
l=list(input().split())
l=[eval(i) for i in l]
l.sort()
print(l[-1])