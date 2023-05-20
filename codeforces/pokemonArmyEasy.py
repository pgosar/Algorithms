for i in range(int(input())):
    n, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = 0
    l = 400000
    r = 0
    mult = True
    for i, val in enumerate(a):
        if mult:
            if val > r:
                r = val
            else:
                ans += r
                mult = False
                l = val
        else:
            if val < l:
                l = val
            else:
                ans -= l
                mult = True
                r = val
    if mult:
        ans += r
    print(ans)
