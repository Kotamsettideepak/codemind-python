a=int(input())
b=str(a)
b=list(b)
b.reverse()
b=''.join(b)
b=int(b)
sa=a*a
sb=b*b
sa=str(sa)
sb=str(sb)
lsa=list(sa)
lsa=''.join(lsa)
lsa=int(lsa)
lsb=list(sb)
lsb.reverse()
nsb=''.join(lsb)
nsb=int(nsb)
if lsa==nsb :
    print("True")
else :
    print("False")
    '''
    a=12
    b='12'
    b=['1','2']
    b=['2','1']
    b='21'
    b=21
    sa=144
    sb=441
    sa='144'
    sb='441'
    lsa=['1','4','4']


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''