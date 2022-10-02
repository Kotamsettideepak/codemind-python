a,b=map(int,input().split())
l1=list(input().split())
l2=list(input().split())
l1=set(l1)
l2=set(l2)
l1=list(l1)
l2=list(l2)
l1.sort()
l2.sort()
lel1=len(l1)
lel2=len(l2)
l1=[eval(i) for i in l1]
l2=[eval(i) for i in l2]
ca=0
cb=0
for i in range(0,lel1):
    if l1[i] not in l2:
        ca+=1
for i in range(0,lel2):
    if l2[i] not in l1:
        cb+=1
print(ca+cb)











































''' 
6 8
l1 = 2 1 2 4 5 7
l2 = 8 8 9 8 9 8 9 9
l1={'1','2','4','5','7'}
l2={'8','9'}
l1=['1','2','4','5','7']
l2=['8','9']
l1=['1','2','4','5','7']
l2=['8','9']
lrl1= 5
lel2=2
l1 =[1,2,4,5,7]
l2=[8,9]


























'''