n, a, b, c = map(int, input().split())
ribbons, i = 0, 0
while i * a <= n:
    j = 0
    while i * a + j * b <= n:
        if (n - i * a - j * b) % c == 0:
            ribbons = max(ribbons, i + j + (n - i * a - j * b) // c)
        j += 1
    i += 1

print(ribbons)
