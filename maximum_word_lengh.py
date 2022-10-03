a=input()
a=list(a.split())
m=0
for i in range(len(a)):
    if m<len(a[i]):
        m=len(a[i])
print(m)