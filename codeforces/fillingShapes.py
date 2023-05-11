n  = int(input())
ways = 0
if n % 2 == 0:
    print(2 ** (n // 2))
else:
    print('0')