# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid?envType=daily-question&envId=2024-10-29


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        #Understanding
        # The problem requires finding the maximum number of moves possible in an `m x n` grid, where each move must follow two rules:
        # Move to one of three cells: right-up `(row-1, col+1)`, right `(row, col+1)`, or right-down `(row+1, col+1)`.
        # The destination cell’s value must be strictly greater than the current cell's value.
        # We start from any cell in the first column and aim to achieve the maximum possible moves.

        #key_observations
        # Since we have only three possible directions for each cell, a recursive approach can efficiently explore all possible moves.
        # To avoid redundant calculations and improve efficiency, we use a memoization table (`memo`) to store the maximum number of moves possible from each cell.
        # Each cell in the memo grid represents the maximum moves starting from that cell, helping to avoid re-evaluations.

        #Approach
        # 1. Memoization Setup : Create a `memo` grid initialized to `-1` to store the maximum moves from each cell.
        # 2. Recursive Function :
            # For each cell `(i, j)`, if the cell’s value is smaller than or equal to the previous cell’s value, return `-inf` as it’s an invalid move.
            # Move in each of the three possible directions (right-up, right, and right-down).
            # Use `memo[i][j]` to store and retrieve already computed maximum moves for efficiency.
        # 3. Final Calculation :
        # Starting from each cell in the first column, call the recursive function to find the maximum moves.
        # Keep track of the maximum moves found across all paths.

        #concepts_used
        # Memoization to store and reuse previously computed results.
        # Depth-First Search (DFS) with a recursive approach for exploring paths.

        #complexities
        # Time Complexity : O(m * n)  
            # Each cell is evaluated once due to memoization, with each cell checking up to 3 possible moves.
        # Space Complexity : O(m * n)  
            # Due to the memoization table and recursive call stack.

        
        m = len(grid)
        n = len(grid[0])

        memo = [[-1] * n for _ in range(m)]

        def findMaxMoves(i, j, prev):

            if memo[i][j] != -1:
                return memo[i][j]

            if grid[i][j] <= prev:
                return -inf
            
            directions = [(-1, 1), (0, 1), (1, 1)]
            
            result = 0
            for r, c in directions:
                new_r = i + r
                new_c = j + c

                if new_r not in range(m) or new_c not in range(n):
                    continue

                result = max(result, 1 + findMaxMoves(new_r, new_c, grid[i][j]))
            
            memo[i][j] = result
            return memo[i][j]

        final_result = 0

        for i in range(m):
            final_result = max(final_result, findMaxMoves(i, 0, -1))
        
        return final_result