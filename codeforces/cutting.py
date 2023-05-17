n, b = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
dp = []
c = [0, 0]
for i in range(n-1):
    c[a[i] & 1] += 1
    if c[0] == c[1]:
        dp.append(abs(a[i+1] - a[i]))
dp = sorted(dp)
print(dp)
for i in dp:
    if i <= b:
        ans += 1
        b -= i
print(ans)
