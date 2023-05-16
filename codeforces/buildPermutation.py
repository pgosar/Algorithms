import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    roots = [1]
    a = [0] * n
    idx = 2
    while roots[-1] < n:
        roots.append(idx ** 2)
        idx += 1
    idx = 0
    for i in range(n-1, -1, -1):
        x = int((2*i)**(1/2))
        y = x*x
        if a[i] == 0 and a[y-i] == 0:
            a[i] = y-i
            a[y-i] = i
    print(*a)
