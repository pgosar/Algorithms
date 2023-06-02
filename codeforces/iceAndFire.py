import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 0
    for i in range(n-1):
        if i == 0 or s[i] == s[i-1]:
            ans += 1
        else:
            ans = 1
        print(i -ans + 2, end=' ')
    print()
