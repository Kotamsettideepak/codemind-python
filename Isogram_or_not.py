def moon(s:str)->bool:
    d={}
    for i in s:
        if i in d:
            return False
        else:
            d[i]=1
    return True

s=input()
print(moon(s))