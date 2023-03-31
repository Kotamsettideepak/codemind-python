a=int(input())
s=input()
s=list(s.split())
s=[eval(i) for i in s]
print(sum(s))