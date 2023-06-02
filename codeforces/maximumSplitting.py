for _ in range(int(input())):
    a=int(input())
    if a<4 or a in [5,7,11]:
        print(-1)
    else:
        print(a // 4 - a % 2)
