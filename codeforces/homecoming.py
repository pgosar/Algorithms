import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, p = map(int, input().split())
    s = input().strip()
    i = len(s)
    sm = 0
    while sm <= p and i > 0:
        i -= 1
        if i == len(s) - 1 or s[i - 1] != s[i]:
            sm += a if s[i - 1] == "A" else b
    print(i + 1)
