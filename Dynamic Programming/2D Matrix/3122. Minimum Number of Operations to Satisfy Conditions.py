# 3122. Minimum Number of Operations to Satisfy Conditions
# https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/description/

# Approach
# Will be checking each column for 0 -> 9
# On current column we take count of value that require to be update if not matching with selected keeping value
# After keeping a certain value for current column we move to next column
# for next column we check all the value except the prev column val
# return the minimum change required

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        
        dp = {}

        def cal(j, val):
            if j == len(grid[0]):
                return 0

            if (j, val) not in dp:

                changeCount = 0
                for i in range(len(grid)):
                    if grid[i][j] != val:
                        changeCount += 1

                result = inf
                for k in range(10):
                    if k != val:
                        result = min(result, changeCount + cal(j + 1, k))

                dp[(j, val)] = result
                
            return dp[(j, val)]
        
        return min(cal(0, i) for i in range(10))