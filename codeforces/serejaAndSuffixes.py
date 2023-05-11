n, m = map(int, input().split())
a = list(map(int, input().split()))
b = set()
for i in range(n):
    b.add(a[n - i - 1])
    a[n - i - 1] = len(b)

for _ in range(m):
    print(a[int(input()) - 1])
