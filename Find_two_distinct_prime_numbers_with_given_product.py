a=int(input())
l=[]
c=0
for i in range(1,a):
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        l.append(i)
    c=0
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]*l[j]==a:
            print(l[i],l[j])
            break
    if l[i]*l[j]==a:
        break
    else:
        c+=1
if c==len(l):
    print(-1)