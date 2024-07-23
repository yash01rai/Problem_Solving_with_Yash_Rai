class Solution:
    def dfs(self, node, graph, visited, stack, curr_path):

        if node in curr_path:
            return False
        
        if node in visited:
            return True

        visited.add(node)
        curr_path.add(node)

        for neighbor in graph[node]:
            if not self.dfs(neighbor, graph, visited, stack, curr_path):
                return False

        curr_path.remove(node)
        stack.append(node)
        return True

    def topological_sort(self, graph, totalNodes):
        curr_path = set()
        visited = set()
        stack = []

        # Visit all nodes
        for node in range(1, totalNodes + 1):
            if not self.dfs(node, graph, visited, stack, curr_path):
                return []

        # Reverse the stack to get the topological order
        return stack[::-1]

    def graphBuilder(self, nodeList):
        graph = defaultdict(list)

        for u, v in nodeList:
            graph[u].append(v)

        return graph


    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        #brainstorm
        # we can use topo logical sort to identify if conditions are valid?
        # so we some how identify the order and then place the elements accordingly
        
        # left most is 3 than 2 than 1 
        # above is left to right order

        # 1 and 3 should be above 2

        # will 1 to k and k * k matrix will ensure that if orders are right the matrix can be form?
        # if true both order doesn't hinder the posibilty of the matrix

        # how to build the matrix ?
        # top-left
        # middle-last
        # last-middle

        # revise topo logical
        # DFS and BFS

        #Understanding
        # We have to return a k x k matrix based on given row and column conditions.
        # The rowCondition will tell the order of 1 to n numbers from left to right.
            # For example, [2, 5] means 2 will be to the left of 5 in the matrix.
        # The colCondition will tell the order of 1 to n numbers from above to below.
            # For example, [3, 2] means 3 will be above 2 in the matrix.
        # return matrix if possible or return empty []

        #key_observations
        # We need to create a matrix in order based on conditions, and there may be cases where the conditions do not allow a valid matrix.
        # The conditions dictate the placement of elements.
        # We can use topological sort to verify the conditions and build the matrix accordingly.

        #Approach
        # 1. Define a k x k matrix with 0 as the initial values of the elements.
        # 2. Build graphs from row and column conditions.
        # 3. Run topological sort on both graphs and get the order if the conditions are valid.
            # If not, return an empty list as the result.
        # 4. Use the valid row and column order to generate the matrix.
        # 5. To generate the matrix, run a nested loop with i and j pointers.
            # When row i and column j values match, update the matrix[i][j] with the current row i or column j value.
        # 6. Return the matrix.

        #Complexities
        # Time Complexity : O(k ^ 2 + m + n)
            # Building the graph takes O(m + n) time, where there are m edges in rowConditions and n edges in colConditions.
            # Topological sort takes O(k + m + n) time.
            # Constructing the result matrix of size k x k takes O(k ^ 2) time.
        # Space Complexity : O(k ^ 2 + m + n)
            # The space required for each graph is O(k + m) and O(k + n).
            # The stack, visited set, and current path set require O(k) space.
            # The matrix size is O(k ^ 2).

        #Topics
        # Array, Graph, Topological Sort, Matrix


        m = len(rowConditions)
        n = len(colConditions)

        result = [[0] * k  for _ in range(k)]

        rowGraph = self.graphBuilder(rowConditions)
        colGraph = self.graphBuilder(colConditions)

        leftRight = self.topological_sort(rowGraph, k)
        topDown = self.topological_sort(colGraph, k)

        if not leftRight or not topDown:
            return []
    
        for i in range(k):
            for j in range(k):
                if leftRight[i] == topDown[j]:
                    result[i][j] = leftRight[i]

        return result