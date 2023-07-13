import bisect

for _ in range(int(input())):
    n, m = map(int, input().split())
    lines = sorted([int(input()) for _ in range(n)])
    for i in range(m):
        a, b, c = map(int, input().split())
        j = bisect.bisect_left(lines, b)
        r = 4 * a * c
        if j < n and (lines[j]-b)**2 < r:
            print("YES")
            print(lines[j])
        elif j > 0 and (lines[j - 1] - b) ** 2 < r:
            print('YES')
            print(lines[j - 1])
        else:
            print('NO')
