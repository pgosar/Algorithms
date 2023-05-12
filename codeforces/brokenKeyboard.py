import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = input()
letters = list(input().split())
t = 0
ans = 0
for i in s:
    print(i)
    if i in letters:
        t += 1
    else:
        ans += (t * (t + 1) // 2)
        t = 0
print(ans)
