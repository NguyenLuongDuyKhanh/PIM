from math import gcd
from math import lcm

def lcm(x, y):
    return x * y // gcd(x, y)

print(lcm(15, 20))
