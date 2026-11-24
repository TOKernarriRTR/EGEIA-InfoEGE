for x in range(1,3000):
    a = 9*11**210 + 8*11**150-x
    n = []
    while a > 0:
        n = [a%11] + n
        a = a//11
    if n.count(0) == 60:
        print(x)

# for x in range(1,3000):
#     a = 9 * 11 ** 210 + 8 * 11 ** 150 - x
#     k = 0
#     while a>0:
#         if a%11 == 0: k+=1
#         a =a //11
#     if k == 60:
#         print(x)

# 2992