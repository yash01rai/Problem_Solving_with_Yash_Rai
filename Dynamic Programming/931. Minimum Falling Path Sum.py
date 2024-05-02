# https://leetcode.com/problems/minimum-falling-path-sum/description/

# Approach 1 dfs
# Will have three recursive calls and minimum will be added to the current values

# optimise using dp

# Approach 2 iterative without using extra space


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        # bottom up done\
        
        n = len(matrix)
        m = len(matrix[0])

        # save the space but data got manipulated
        dp = matrix.copy()

        for i in range(n - 2, -1, -1):
            for j in range(m - 1, -1, -1):
                mini = dp[i + 1][j] 

                if j + 1 in range(m):
                    mini = min(dp[i + 1][j + 1], mini)

                if j - 1 in range(m):
                    mini = min(dp[i + 1][j - 1], mini)
                
                dp[i][j] = mini + dp[i][j]
        
        ans = inf
        for x in dp[0]:
            ans = min(x, ans)
        
        return ans
                

        # dp = {}

        # def dfs(i, j):

        #     if (i, j) in dp:
        #         return dp[(i, j)]

        #     if i not in range(n):
        #         return 0
            
        #     if j not in range(m):
        #         return inf
            
        #     directions = [(1, 1), (1, 0), (1, -1)]

        #     mini = inf
        #     for row, col in directions:
        #         new_row = i + row
        #         new_col = j + col
                
        #         mini = min(mini, matrix[i][j] + dfs(new_row, new_col))
            
        #     dp[(i, j)] = mini
        #     return dp[(i, j)]

        # ans = float('inf')

        # for i in range(n): 
        #     for j in range(m):
        #         ans = min(dfs(i, j), ans)
            
        #     break

        # return ans

