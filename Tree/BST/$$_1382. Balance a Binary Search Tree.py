# Question Link -> https://leetcode.com/problems/balance-a-binary-search-tree/?envType=daily-question&envId=2024-06-26

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        # Topics
        # Recursion, Depth-First Search (DFS)
        # In-order traversal:
        #    1. Explore the left sub-tree
        #    2. Visit the current node
        #    3. Explore the right sub-tree
        # In-order traversal of a binary search tree (BST) helps us retrieve values in non-decreasing order.

        # Approach
        # We'll get the node values stored in an array using DFS.
        # then, using DFS again, we'll create a tree by seeking the middle value of the array as the root value.
        # then, we'll perform recursion on both left and right side, start -> mid - 1 and mid + 1 -> end
        # assigning recursive calls to node.left and node.right.

        nodes = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)
        
        dfs(root)


        def dfs(start, end):
            if start > end:
                return
            
            mid = (start + end) // 2
            node = TreeNode(nodes[mid])
            node.left = dfs(start, mid - 1)
            node.right = dfs(mid + 1, end)

            return node
        
        return dfs(0, len(nodes) - 1)