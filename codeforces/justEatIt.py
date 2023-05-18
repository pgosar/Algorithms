import sys
input = sys.stdin.readline

def check(n, a):
    s, sm = sum(a), 0
    for i in range(n-1):
        sm += a[i]
        if sm >= s or sm <= 0:
            return "NO"
    return "YES"

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(check(n, a))
