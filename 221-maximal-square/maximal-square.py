class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        def helper(r,c):
            if matrix[r][c]=='0':
                return 0
            
            cur = int(matrix[r][c])
            if (r+1)==rows or (c+1)==cols:
                return cur
            
            right = matrix[r][c+1]
            down = matrix[r+1][c]
            diag = matrix[r+1][c+1]

            cur = cur + min(right, down, diag)
            return cur
        
        res = 0
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                matrix[r][c] = helper(r,c)
                res = max(res, matrix[r][c])
        
        return res**2