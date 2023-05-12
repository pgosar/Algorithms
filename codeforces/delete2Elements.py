for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    d = {}
    ans = 0
    target = sum(arr) / n
    for i in arr:
        need = 2 * target - i
        ans += d.get(need, 0)
        d[i] = d.get(i, 0) + 1
    print(ans)
