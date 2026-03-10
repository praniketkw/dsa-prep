class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while True:
            if i*i<=n:
                squares.append(i*i)
                i+=1
            else:
                break
        
        dp = [n]*(n+1)
        dp[0]=0

        for a in range(1,n+1):
            for s in squares:
                if s<=a:
                    dp[a] = min(dp[a],1+ dp[a-s])
                else:
                    break
        
        return dp[n]
