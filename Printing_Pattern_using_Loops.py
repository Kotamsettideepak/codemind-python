a=int(input())
c=a
d=a
r=a+(a-1)
l=[[0]*r]*r #                
l[0]=[a]*r            
for i in range(1,(r//2)): 
    b=[0]*r             #    
    d=a #       
    for j in range(i): #    
        b[j]=d#   
        b[-j-1]=d#   
        d-=1#                           
    for m in range(i,r-i):#          
        b[m]=d#                     
    x=list(b)#
    l[i]=x#
b=[0]*r
for i in range(r//2):
    b[i]=c
    b[-i-1]=c
    c-=1
b[(r//2)]=1
l[(r//2)]=b
for i in range(r//2):
    l[-i-1]=l[i]
for i in l:
    b=list(i)
    for j in b:
        print(j,end=' ')
    print()