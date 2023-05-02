a=int(input())
b=int(a)
a=str(a)
temp =list(a)
max=0
for i in range(len(a)):
    a=list(temp)
    if a[i]=="6":
        a[i]="9"
        a=''.join(a)
        a=int(a)
        if a>b:
            b=a
    else :
        a[i]="6"
        a=''.join(a)
        a=int(a)
        if a > b:
            b=a
print(b)