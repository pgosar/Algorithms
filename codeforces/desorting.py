for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dif = float('inf')
    for i in range(n-1):
        dif = min(dif, a[i+1]-a[i])
    print(0 if dif < 0 else dif//2+1)
