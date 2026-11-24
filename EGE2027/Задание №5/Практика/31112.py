for x in range(1,10000):
    b = bin(x)[2:]
    if x % 2 == 0:
        b = '11' + b + '11'
    else:
        b = '1' +b + '00'
    r = int(b,2)
    if r <= 113:
        print(r)


# 108