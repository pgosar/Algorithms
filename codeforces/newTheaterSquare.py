for _ in range(int(input())):
    price = 0
    n, m, x, y = map(int, input().split())
    s = ' '.join([input() for _ in range(n)])
    if x * 2 <= y:
        print(x * s.count('.'))
    else:
        a = s.count('..')
        b = s.count('.') - a * 2
        print(a * y + b * x)