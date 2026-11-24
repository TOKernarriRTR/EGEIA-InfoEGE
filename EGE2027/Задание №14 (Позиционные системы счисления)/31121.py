m = 0
for x in range(1,2030):
    a = 5**150+5**100-x
    k = 0
    while a > 0:
        if a%5 == 0: k+=1
        a = a//5
    if k >= m:
        print(m,x)
        m = k


# 1875