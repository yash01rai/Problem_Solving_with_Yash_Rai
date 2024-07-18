# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

       
        #Understanding
        # Given the root of a binary tree, where all the nodes have distinct values.
        # We need to delete all the nodes whose values are found in the given to_delete list.

        #key_observations
        # Deleting a node from the tree means not only removing the connection to its child nodes but also removing the connection with its parent node.
        # This also means we can't just remove the first node we encounter in to_delete as we perform DFS.
        # We need to start exploring the tree and remove nodes only after we are done visiting their children.
        # We can do this by rebuilding the tree using recursion and removing the nodes.

        #Approach
        # We will perform DFS postorder traversal as per the observations.
        # Visit the left subtree and then the right subtree.
        # If our current node's value is found in to_delete:
            # We append the left node to our result and disconnect the left node.
            # The same actions would be performed for the right node.
            # We remove the current node's value from to_delete.
            # We return None to our parent node.
        # If the current node's value is not found in to_delete, we return the current node to its parent.
        # Check for the root node separately and return the result.

        #Complexities
        # Time Complexity: O(N)
            # Visiting N nodes once.
        # Space Complexity: O(N)
            # Recursion call stack.
            # Using a set to search to_delete values.

        #Topics
        # Array, Hash Table, Tree, Depth#First Search, Binary Tree

        to_delete = set(to_delete)
        result = []

        def findAllTheTrees(node):
            if not node:
                return None

            node.left = findAllTheTrees(node.left)
            node.right = findAllTheTrees(node.right)

            if node.val in to_delete:
                if node.left:
                    result.append(node.left)
                    node.left = None
                
                if node.right:
                    result.append(node.right)
                    node.right = None
                
                to_delete.remove(node.val)
                return None
            
            return node
        
        isRootRemoved = findAllTheTrees(root)

        if isRootRemoved:
            result.append(root)

        return result