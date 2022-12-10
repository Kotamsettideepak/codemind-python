def tens(a):
    if a==10:
        return "ten"
    if a==20:
        return "twenty"
    if a==30:
        return "thirty"
    if a==40:
        return "forty"
    if a==50:
        return "fifty"
    if a==60:
        return "sixty"
    if a==70:
        return "seventy"
    if a==80:
        return "eighty"
    if a==90:
        return "ninety"
def single(a):
    if a==1:
        return "one"
    if a==2:
        return "two"
    if a==3:
        return "three"
    if a==4:
        return "four"
    if a==5:
        return "five"
    if a==6:
        return "six"
    if a==7:
        return "seven"
    if a==8:
        return "eight"
    if a==9:
        return "nine"

def double(a,l):
    a=str(a)
    b=int(a)
    a=list(a)
    a=[eval(i) for i in a]
    if a[1]==0 and a[0]!=0:
        a=b
        c=tens(a)
        return c
    if a[0]==0 and a[1]!=0:
        a=a.remove(a[0])
        c=single(a[1])
        return c
    a=b
    if a==11:
        return "eleven"
    if a==12:
        return "twelve"
    if a==13:
        return "thirteen"
    if a==14:
        return 'fourteen'
    if a==15:
        return "fifteen"
    if a==16:
        return "sixteen"
    if a==17:
        return "seventeen"
    if a==18:
        return "eighteen"
    if a==19:
        return "nineteen"
    b=list(str(a))
    b=[eval(i) for i in b]
    c= tens(b[0]*10)+" "+single(b[1])
    return c


def triple (a,l):
    b=int(a)
    a=str(a)
    a=list(a)
    a=[eval(i) for i in a]
    if b%100==0:
        c= single(a[0])+' '+"hundred"
        return c
    else:
        a.remove(a[0])
        a=[str(i) for i in a]
        if a[0]=='0':
            a=''.join(a)
            a=int(a)
            c= single(b//100)+' '+"hundred"+" "+single(a)
            return c
        a=''.join(a)
        a=int(a)
        c= single(b//100)+' '+"hundred"+" "+double(a,2)
        return c


def quad(a,l):
    b=int(a)
    a=str(a)
    a=list(a)
    a=[eval(i) for i in a]
    if b%1000==0:
        c= single(a[0])+' '+"thousand"
        return c    
    else :
        a.remove(a[0])
        a=[str(i) for i in a]
        if a[0]=='0' and a[1] !='0':
            a=''.join(a)
            a=int(a)
            c= single(b//1000)+' '+"thousand"+" "+double(a,3)
            return c 
        elif a[0]=='0' and a[1]=='0':
            a=''.join(a)
            a=int(a)
            c= single(b//1000)+' '+"thousand"+" "+single(a)
            return c            
        a=''.join(a)
        a=int(a)
        c= single(b//1000)+' '+"thousand"+" "+triple(a,3)
        return c



a=int(input())
a=str(a)
a=list(a)
l=len(a)
a=''.join(a)
a=int(a)
if l==1:
    b=single(a)
if l==2:
    b=double(a,l)
if l==3:
    b=triple(a,l)
if l==4:
    b=quad(a,l)
print(b)