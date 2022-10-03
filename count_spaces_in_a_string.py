a=input()
a=list(a)
c=0
for i in range(len(a)):
    if ' ' ==a[i]:
        c+=1
print(c)