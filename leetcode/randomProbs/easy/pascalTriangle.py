class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        dp = [[1], [1, 1]]
        for i in range(2, numRows):
            lis = [1]        
            for j in range(i - 1):
                lis.append(dp[i-1][j] + dp[i-1][j + 1])
            lis.append(1)
            dp.append(lis)
        return dp
