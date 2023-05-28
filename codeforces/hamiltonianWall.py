import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s1 = input().strip()
    s2 = input().strip()
    c1, c2 = 1, 1
    for i in range(n):
        if s1[i] == s2[i]:
            c1, c2 = c2, c1
        elif s1[i] == 'B':
            c2 = 0
        else:
            c1 = 0
    if c1 or c2:
        print("YES")
    else:
        print("NO")
