# https://leetcode.com/problems/lucky-numbers-in-a-matrix

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        #Understanding
        # Given a matrix, we need to return all the lucky numbers.
        # A lucky number is an element of the matrix such that it is the minimum element in its row and the maximum in its column.

        #key_observations
        # If you observe carefully, you will find that there will be at most one lucky number per matrix.

        #Approach
        # 1. First, iterate through each row of the matrix.
        # 2. Take the minimum value of the current row.
        # 3. Maintain a variable to keep track of the maximum of all the minimum values found in each row.
        # 4. This ensures that the number we are selecting is the minimum number of a row and the maximum number of its column.
        # 5. Second, go through each column and get the maximum value of each column.
        # 6. Maintain a variable to keep track of the minimum of all the maximum values from each column.
        # 7. If the min-max row value is equal to the max-min column value, return that value as the answer.
        # 8. Otherwise, return an empty list [].

        #Complexities
        # Time Complexity: O(N * M)
            # Iterating through each element of the matrix a constant number of times.
        # Space Complexity: O(1)
            # Constant space is used.

        #Topics
        # Array, Matrix

        
        # observation is only 1 number
        n = len(matrix)
        m = len(matrix[0])

        rowMin_colMax = -inf
        for row in matrix:
            rowMin = min(row)
            rowMin_colMax = max(rowMin_colMax, rowMin)
        
        colMax_rowMin = inf
        for i in range(m):
            colMax = max(matrix[j][i] for j in range(n))
            colMax_rowMin = min(colMax_rowMin, colMax)

        if rowMin_colMax == colMax_rowMin:
            return [rowMin_colMax]
        else:
            return []



        # brute force
        m = len(matrix)
        n = len(matrix[0])

        minInRow = [min(row) for row in matrix]
        maxInCol = set()

        for j in range(n):
            currMax = 0
            for i in range(m):
                currMax = max(currMax, matrix[i][j])

            maxInCol.add(currMax)

        result = []


        for i in range(m):
            if minInRow[i] in maxInCol:
                result.append(minInRow[i])
        
        return result

            