from string import *
for x in printable[:27]:
    a = int(f"AB{x}CD",27) + int(f"AP{x}DK",27)
    if a % 26 == 0:
        print(x,a//13)
# 873060