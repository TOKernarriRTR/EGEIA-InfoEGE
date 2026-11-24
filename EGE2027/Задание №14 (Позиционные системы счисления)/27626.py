m = 0
for x in range(1,2030):
    a = 6**2030+6**100-x
    k = 0
    while a > 0:
        if a%6==0: k+=1
        a = a//6
    if k>= m:
        print(k,x)
        m = k

# 1930