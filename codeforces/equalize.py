import sys
input = sys.stdin.readline

n = int(input())
a, b, ans, i = input(), input(), 0, 0
while i < n:
    if a[i] != b[i]:
        if i != n-1 and a[i+1] == b[i] and a[i] == b[i+1]:
            ans += 1
            i += 1
        else:
            ans += 1
    i += 1

print(ans)
