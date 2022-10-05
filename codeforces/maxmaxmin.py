n, k = map(int, input().split())
arr = list(map(int, input().split()))
if k == 1:
    print(min(arr[0:n]))
elif k == 2:
    print(max(arr[0], arr[n-1]))
else:
    print(max(arr[0:n]))
