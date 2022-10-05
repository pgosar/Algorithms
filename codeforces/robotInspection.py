count, n, weight = 0, int(input()), list(map(int, input().split()))
for i in weight:
    if sum([j + (i / j) if i % j == 0 else 0 for j in range(1, int((i - 1) ** 0.5) + 1)]) / 2 == i:
        count += 1
print(count)
