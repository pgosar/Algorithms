import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
ans = [1] * n

for i in range(1, n):
    if a[i] <= a[i - 1] * 2:
        ans[i] = ans[i - 1] + 1
print(max(ans))
