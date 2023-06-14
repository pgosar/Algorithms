class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def dfs(cur, memo):
            curt = tuple(cur)
            if curt in memo:
                return memo[curt]
            cost = sum(cur[i]*price[i] for i in range(len(needs)))
            for s in special:
                tmp = [cur[i] - s[i] for i in range(len(needs))]
                if min(tmp) >= 0:
                    cost = min(cost, dfs(tmp, memo)+s[-1])
            memo[curt] = cost
            return cost
        return dfs(needs, dict())
