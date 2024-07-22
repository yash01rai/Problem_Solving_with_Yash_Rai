# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/?envType=daily-question&envId=2024-07-20

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        #Understanding
        # Given two lists, rowSum and colSum, where rowSum contains the sum of each row and colSum contains the sum of each column.
        # We need to build a 2D matrix of non-negative integers of size rowSum.length * colSum.length.

        #key_observations
        # After observation, you might think about putting the whole rowSum or colSum into the first position.
        # You are on the right track, we will greedily fill the matrix while keeping in mind that both row and column sums are satisfied.

        #Approach
        #1. First, create a result matrix of size n * m.
        #2. Now create two pointers, i and j, starting from 0.
        #3. While the pointers are within size, we perform the following operations:
        # Choose the minimum value from rowSum[i] and colSum[j] and assign it to result matrix[i][j].
        # Then, subtract matrix[i][j] from the current rowSum[i] and current colSum[j], marking that we utilized this much value.
        # Move the pointer i if rowSum[i] is 0, and if colSum[j] is 0, move pointer j.
        #4. At the end, return the result matrix.

        # Complexities
        # Time Complexity: O(N * M)
        # Space Complexity: O(1)

        # Topics
        # Array, Greedy, Matrix

        m = len(rowSum)
        n = len(colSum)

        resultMatrix = [[0] * n for i in range(m)]

        i = 0
        j = 0

        while i < m and j < n:

            resultMatrix[i][j] = min(rowSum[i], colSum[j])

            rowSum[i] -= resultMatrix[i][j]
            colSum[j] -= resultMatrix[i][j]

            if rowSum[i] == 0:
                i += 1
            
            if colSum[j] == 0:
                j += 1
        
        return resultMatrix
