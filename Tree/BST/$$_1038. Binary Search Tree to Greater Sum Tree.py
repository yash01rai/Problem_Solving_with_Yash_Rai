# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/?envType=daily-question&envId=2024-06-25

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        # Amazon

        # in-order traversal is sorted for bst
        total_sum = 0
        def dfs(node):
            nonlocal total_sum

            if not node:
                return 0


            right = dfs(node.right)

            total_sum += node.val
            node.val = total_sum

            left = dfs(node.left)

        dfs(root)
        return root