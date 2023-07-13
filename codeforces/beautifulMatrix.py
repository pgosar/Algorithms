print(abs((x := next((i, j) for i in range(5) for j, num in enumerate(input().split()) if int(num) == 1))[0] - 2) + abs(x[1] - 2))
