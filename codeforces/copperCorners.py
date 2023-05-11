s = int(input())
copper = [list(map(int, input().split())) for _ in range(s)]
if (s == 1):
    print(copper[0][0])
else:
    print(copper[0][0] + copper[0][s - 1] + copper[s - 1][0] + copper[s - 1][s - 1])
