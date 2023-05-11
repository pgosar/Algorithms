for _ in range(int(input())):
    n = int(input())
    ans = 0
    while n >= 2:
        a = 2
        adder = 5
        while a + adder <= n:
            a += adder
            adder += 3
        n -= a
        ans += 1
    print(ans)
