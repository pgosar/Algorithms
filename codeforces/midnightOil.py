n, k = map(int, input().split(" "))

left = 0
right = n
mid = 0

def helper(v):
    ans = v
    while v > 0:
        v //= k
        ans += v
    return ans >= n

while left < right:
    mid = (left + right) // 2
    if helper(mid):
        right = mid
    else:
        left = mid + 1
print(int(left))
