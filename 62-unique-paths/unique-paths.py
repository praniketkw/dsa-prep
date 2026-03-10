class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(m)] for j in range(n)]

        dp[n-1][m-1] = 1
        for r in range(n):
            dp[r][m-1]=1
        for c in range(m):
            dp[n-1][c] = 1
        
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                dp[i][j] = dp[i][j+1]+dp[i+1][j]
        
        return dp[0][0]