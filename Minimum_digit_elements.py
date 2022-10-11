a=int(input())
l=list(input().split())
# print(l)
o=list(l[0])
ln=len(o)
for i in range(len(l)):
    b=list(l[i])
    if len(b)<ln:
        ln=len(b)
c=0
for i in range(len(l)):
    b=list(l[i])
    if ln==len(b):
        c+=1
print(c)