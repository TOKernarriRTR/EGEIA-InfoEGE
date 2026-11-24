from functools import *

def f(n):
    return g(n-50000) + g(n+50000)

@lru_cache(None)
def g(n):
    if n<=6: return 5**n
    return g(n-3)+2
for x in range(1,200000): g(x)
print(f(100000))

# 152076