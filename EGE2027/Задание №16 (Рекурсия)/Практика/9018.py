from functools import *
@lru_cache(None)
def f(n):
    if n < 15: return 5
    return (n+6)*f(n-4)
for x in range(12,230000,3): f(x)
print((f(223561)//327+f(223549)//177)//f(223537))

# 56761450