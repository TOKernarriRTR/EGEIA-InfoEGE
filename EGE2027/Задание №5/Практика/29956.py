m = []
def C3(a):
    s = ''
    while a>0:
        s = str(a%3) + s
        a = a//3
    return s
for x in range(1,10000):
    b = C3(x)
    if x % 3 == 0:
        b = '1' + b + '02'
    else:
        b = b + C3(5*(x%3))
    r = int(b,3)
    if r >= 177:
        m.append(x)
print(min(m))

# 8
