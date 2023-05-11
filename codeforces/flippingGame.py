n = int(input())
coins = list(map(int, input().split()))
sum = sum(coins)
dp = -1
for i in range(n):
    for j in range(i + 1):
        temp = sum
        for s in range(i, j + 1):
            if coins[s] == 1:
                s -= 1
            if coins[s] == 0:
                s += 1
        dp = max(temp, dp)
print(dp)

# 4
# 1 0 0 1
# i 0       1       2       3      4
# j 0 1
# a 1 0 0 1 
# ans 0
