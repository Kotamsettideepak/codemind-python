n = int(input())
l = list(map(int, input().split()))
k = int(input())
for i in range(k):
    r = []
    r.append(l[-1])
    for j in range(len(l)-1):
        r.append(l[j])
    l = r
print(*l)
