for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 1:
        print(-1)
    else:
        b = []
        for i in range(0, len(a), 2):
            if a[i] == a[i+1]:
                b += [i+1, i+2]
            else:
                b += [i+1, i+1, i+2, i+2]
        print(len(b) // 2)
        for i in range(0, len(b), 2):
            print(b[i], b[i+1])

