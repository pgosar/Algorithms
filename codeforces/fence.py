n, k = map(int, input().split())
heights = list(map(int, input().split()))
min = tmp = sum(heights[:k])
j = 0
for i in range(n - k):
    tmp += heights[i + k] - heights[i]
    if tmp < min:
        min = tmp
        j = i + 1
print(j+1)
