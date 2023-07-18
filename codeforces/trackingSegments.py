for _ in range(int(input())):
    n, m = map(int, input().split())
    bounds = [tuple(map(int, input().split())) for _ in range(m)]
    q = int(input())
    vals = list(int(input()) for _ in range(q))

    def check(m):
        a = [0] + [-1] * n
        for i in range(m):
            a[vals[i]] = 1
        for i in range(n):
            a[i+1] += a[i]
        for l, r in bounds:
            if a[r] > a[l-1]:
                return True
        return False
    if not check(q):
        print(-1)
    else:
        l, r = 0, q
        while r-l > 1:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m
        print(r)
