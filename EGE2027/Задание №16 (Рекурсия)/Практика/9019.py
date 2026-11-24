from functools import *
@lru_cache(None)
def f(n):
    if n < 12: return 3
    return (n+7) * f(n-4)
for x in range(1,350000,8): f(x)
print((f(341569)//336 + f(341561)//576) // f(341557))

# 32402129