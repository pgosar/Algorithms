import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    x, ans = a[i], float('inf')
    for i in range(16):
        for j in range(16):
            if ((x+i) << j) % 32768 == 0:
                ans = min(ans, i+j)
    print(ans)
