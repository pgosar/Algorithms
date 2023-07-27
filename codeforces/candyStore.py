import sys
from math import *

input = sys.stdin.readline
for _ in range(int(input())):
    ans, a, b = 1, 0, 1
    for _ in range(int(input())):
        x, y = map(int, input().split())
        a = gcd(a, x*y)
        b = lcm(y, b)
        if a % b != 0:
            ans += 1
            a = x*y
            b = y
    print(ans)
