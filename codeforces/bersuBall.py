n = input()
b = list(map(int, input().split()))
m = input()
g = list(map(int,input().split()))
b.sort()
g.sort()
m=0
for i in range(len(b)):
    for j in range(len(g)):
        if abs(g[j] - b[i]) <= 1:
            m += 1
            g[j] = -10
            break
print(m)
