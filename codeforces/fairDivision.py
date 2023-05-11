t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES") if (len(arr) % 2 == 0 or arr.count(1) > 0) and sum(arr) % 2 == 0 else print("NO")