a=int(input())
for j in range(a):
    b=chr(65+j)
    c=[b]*a
    for m in c:
        print(m,end=' ')
    print()