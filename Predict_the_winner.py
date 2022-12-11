a=int(input())
l=list(map(int,input().split()))
#print(l)
r=list(l)
y=[]
r=[r[i] for i in range(len(r)//2)]
for i in range(-1,-((len(l)//2)+1),-1):
    y.append(l[i])
r=sum(r)-sum(y)
if r%4==0:
    print("X")
else :
    print("Y")
