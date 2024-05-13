# https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float: 

        # Optimized bottom up
        # Define possible directions for the knight's moves
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                      (2, 1), (2, -1), (-2, 1), (-2, -1)]

        prevBoard = [[0] * n for _ in range(n)]
        prevBoard[row][column] = 1

        for moves in range(1, k + 1):
            currBoard = [[0] * n for _ in range(n)]

            for i in range(n):
                for j in range(n):

                    for x, y in directions:
                        prev_i = i - x
                        prev_j = j - y

                        if 0 <= prev_i < n and 0 <= prev_j < n:
                            currBoard[i][j] += prevBoard[prev_i][prev_j] / 8
            
            prevBoard = currBoard
        
        totalProbability = sum(prevBoard[i][j] for i in range(n) for j in range(n))
        return totalProbability

        # Time complexity: O(k * n^2)
        # Space complexity: O(n ^ 2)



        # Define possible directions for the knight's moves
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                      (2, 1), (2, -1), (-2, 1), (-2, -1)]

        # Initialize the dynamic programming table
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1 # intial position

        # Iterate over the number of moves
        for moves in range(1, k + 1):
            # Iterate over the cells on the chessboard
            for i in range(n):
                for j in range(n):
                    # Iterate over possible directions
                    for x, y in directions:
                        prev_i, prev_j = i - x, j - y
                        # Check if the previous cell is within the chessboard
                        if 0 <= prev_i < n and 0 <= prev_j < n:
                            # Add the previous probability
                            dp[moves][i][j] += dp[moves - 1][prev_i][prev_j]

                    # Divide by 8
                    dp[moves][i][j] /= 8

        print(dp)
        # Calculate total probability by summing probabilities for all cells
        total_probability = sum(dp[k][i][j] for i in range(n) for j in range(n))

        return total_probability

        dp = {}

        # Helper function to check if a cell is within the chessboard
        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < n

        # Recursive function to simulate the knight's moves
        def dfs(x, y, k):
            # Base case: if the knight has made all moves, return 1 if on the board, else 0
            if k == 0:
                return 1 if is_valid(x, y) else 0
            
            if (x, y, k) not in dp:
                probability = 0

                # Eight possible moves for the knight
                moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

                for dx, dy in moves:
                    new_x, new_y = x + dx, y + dy
                    probability += 0.125 * dfs(new_x, new_y, k - 1) if is_valid(new_x, new_y) else 0

                dp[(x, y, k)] = probability

            return dp[(x, y, k)]

        return dfs(row, column, k)