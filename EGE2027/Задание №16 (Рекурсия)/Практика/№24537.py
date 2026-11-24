from functools import *
@lru_cache(None)
def f(n):
    if n < 10: return n+10
    return f(n-8) + 2**n
for x in range(1,5000): f(x)
print((f(4000) + 2*f(3992))/f(3984))