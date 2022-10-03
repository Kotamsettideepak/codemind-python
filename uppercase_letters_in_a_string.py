a=input()
# print(a)
a=list(a)
# print(a)
c=0
for i in range(65,91):
    d=chr(i)
    for j in range(0,len(a)):
        if d==a[j]:
            c+=1
print(c)