import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = 0
write = 0
for i in range(n):
    if t[i] == 1:
        write += a[i]
        a[i] = 0
ans = sum(a[:k])
tmp = ans
for i in range(k, n):
    tmp -= a[i-k]
    tmp += a[i]
    ans = max(ans, tmp)
print(ans+write)
