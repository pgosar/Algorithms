import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    t = input().strip()
    flag = False
    for i in range(len(s)):
        r = s[:i+1] + s[:i][::-1]
        if t in r:
            print("YES")
            flag = True
            break
    if not flag:
        print("NO")


