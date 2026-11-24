f = open('31506.txt')
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    a1 = [x for x in a if a.count(x)==1]
    if 2*(a[0]+a[4]) > a[1]+a[2]+a[3] and len(a1) == 5:
        k +=1
print(k)