n = int(input())
costs = list(map(int, input().split()))
costs_sorted = sorted(costs)
m = int(input())

for i in range(1, len(costs_sorted)):
    costs_sorted[i] += costs_sorted[i - 1]

for i in range(1, len(costs)):
    costs[i] += costs[i - 1]

for _ in range(m):
    type, l, r = map(int, input().split())
    if type == 1:
        print(costs[r - 1] - costs[l - 2] if l > 1 else costs[r - 1])
    else:
        print(costs_sorted[r - 1] - costs_sorted[l - 2] if l > 1 else costs_sorted[r - 1])

