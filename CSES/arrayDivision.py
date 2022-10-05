n, k = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
mx = max(arr)
ans = float("inf")
right = 1e18
left = mx
mid = 0

while left <= right:
    mid = (left + right) // 2
    count = 1
    temp = 0
    for i in arr:
        if temp + i > mid:
            count += 1
            temp = 0
        temp += i
    if count <= k:
        if mid < ans:
            ans = mid
        right = mid - 1
    else:
        left = mid + 1


print(int(ans))
