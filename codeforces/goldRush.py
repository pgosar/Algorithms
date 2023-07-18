import sys
input = sys.stdin.readline

def solve(n, m):
    if n == m:
        return True
    if n % 3:
        return False
    return solve(n//3, m) or solve(2*n//3, m)


for _ in range(int(input())):
    n, m = map(int, input().split())
    print("YES" if solve(n, m) else "NO")
