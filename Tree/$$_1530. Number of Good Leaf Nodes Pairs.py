# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # required only for graph solution
    def graphBuilder(self, node, parent, adjList, leafNodes):

        if not node:
            return
            
        if not node.left and not node.right:
            leafNodes.add(node)
        
        if parent:
            adjList[parent].append(node)
            adjList[node].append(parent)

        self.graphBuilder(node.left, node, adjList, leafNodes)
        self.graphBuilder(node.right, node, adjList, leafNodes)

    def countPairs(self, root: TreeNode, distance: int) -> int:

        #Understanding
        # Given the root of a binary tree, we need to return the number of good leaf node pairs.
        # Good leaf node pairs are pairs whose distance between them is equal to or less than the given valid distance.

        #key_observations
        # The focus is on the leaf nodes.
        # There are several ways to solve this problem:
        # 1. Convert the graph and perform BFS traversal from each leaf node to calculate the distance and add valid pairs.
        # 2. Use the concept of LCA (Lowest Common Ancestor) nodes to find the shortest path between pairs satisfying the condition.

        # Approach 1
        # First, build a graph using DFS and an adjacency list.
        # Iterate over the list of leaf nodes and perform BFS to calculate the distances:
        # In BFS, add (leaf node, current distance) to a deque and maintain a visited node set.
        # While the deque is not empty, pop from the left of the deque.
        # Iterate through the neighboring nodes of the popped node.
        # If a neighbor node is not in visited, add the neighbor to visited and check if the current distance + 1 is a valid distance.
        # If yes, add the neighbor to the deque with the new distance.
        # Also, if the neighbor is a leaf node, increase the pair count by 1.
        # After iterating through all the leaf nodes, halve the counter pairs because the count using BFS would be done twice due to the pair nature of the problem.
        # return the pairs

        #Complexities
        # Time Complexity: O(N^2)
            # In the worst case, running BFS on each leaf node will traverse the graph N times.
        # Space Complexity: O(N)
            # For the adjacency list and BFS queue/visited set.


        #Topics
        # Tree, Depth-First Search, Binary Tree, BFS

        # graph solution
        adjList = defaultdict(list)
        leafNodes = set()
        
        # creating graph for traversal
        self.graphBuilder(root, None, adjList, leafNodes) # O(N)

        result = 0
        for leafNode in leafNodes:
            
            # bfs on every single leaf node O(N ^ 2)
            dq = deque()
            dq.append((leafNode, 0))

            visited = set()
            visited.add(leafNode)

            while dq:
                current_node, dist = dq.popleft()

                for neighbor in adjList[current_node]:

                    if neighbor not in visited:
                        visited.add(neighbor)

                        if dist + 1 <= distance:
                            dq.append((neighbor, dist + 1))

                            if neighbor in leafNodes:
                                result += 1
        
        result //= 2
        return result


        #Approach 2 (Using LCA concept) -> O(N ^ 3)
        totalPairs = 0

        def dfs(node):
            nonlocal totalPairs

            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]

            left_dist = dfs(node.left)
            right_dist = dfs(node.right)

            for d1 in left_dist:
                for d2 in right_dist:
                    if d1 + d2 <= distance:
                        totalPairs += 1
            
            all_dist = left_dist + right_dist
            return [d + 1 for d in all_dist]

        dfs(root)
        return totalPairs

        #Approach 3 -> (slightly optimized) O(N * d^3) 
        totalPairs = 0
        def dfs(node):
            nonlocal totalPairs

            if not node:
                return defaultdict(int)
            
            if not node.left and not node.right:
                count = defaultdict(int)
                count[1] += 1
                return count

            left_dist = dfs(node.left)
            right_dist = dfs(node.right)

            for d1 in left_dist:
                for d2 in right_dist:
                    if d1 + d2 <= distance:
                        totalPairs += left_dist[d1] * right_dist[d2]

            
            all_dist = defaultdict(int)
            for d in left_dist:
                if d + 1 <= distance:
                    all_dist[d + 1] = left_dist[d]
            
            for d in right_dist:
                if d + 1 <= distance:
                    all_dist[d + 1] += right_dist[d]
                    
            return all_dist

        dfs(root)
        return totalPairs