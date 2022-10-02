a=input()
l=list(a)
c=0
for i in range(0,len(l)):
    for j in range( 0,len(l)):
        if l[i]==l[j]:
            c+=1
if c==len(l):
    print("True")
else :
    print("False")