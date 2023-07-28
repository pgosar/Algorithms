import sys
input = sys.stdin.readline


def solve(s, i, j):
    ans = 0
    for c in s:
        if c == str(i):
            i, j = j, i
            ans += 1
    if i != j and ans % 2 == 1:
        ans -= 1
    return ans


for _ in range(int(input())):
    s = input().strip()
    ans = 0
    for i in range(10):
        for j in range(10):
            ans = max(ans, solve(s, i, j))
    print(len(s)-ans)
