class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amount = amount + 1
        solutions = [0] * amount
        solutions[0] = 1
        for coin in coins:
            for j in range(coin, amount):
                solutions[j] += solutions[j - coin]
        return solutions[-1]
