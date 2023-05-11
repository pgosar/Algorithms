t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = a[0]
    tmp = a[0]
    sum = 0
    for i in a:
        if tmp * i < 0:
            sum += tmp
            tmp = i
        else:
            tmp = max(tmp, i)
    print(sum + tmp)
