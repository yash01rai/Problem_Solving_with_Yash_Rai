# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/?envType=daily-question&envId=2024-07-16

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLCANode(self, node, startValue, destValue):
        if not node:
            return None

        # if you find one of src or dest node return the node
        if node.val == startValue or node.val == destValue:
            return node

        left = self.findLCANode(node.left, startValue, destValue)
        right = self.findLCANode(node.right, startValue, destValue)

        # if you are getting left node and right node, that means you found the common ancestor, return the current node
        if left and right:
            return node
        
        return left if left else right

    def findPath(self, node, target, path):
        if not node:
            return False
        
        if node.val == target:
            return True
        
        path.append("L")
        if self.findPath(node.left, target, path):
            return True
        path.pop() # backtrack


        path.append("R")
        if self.findPath(node.right, target, path):
            return True
        path.pop() # backtrack

        return False
    

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        #Topics
        # String, Tree, Depth-First Search, Binary Tree

        #Understanding
        # For a given tree, we need to find the shortest path from startValue to destValue.
        # The path should be represented using "L", "R", and "U".
        # "L" -> go to the left node
        # "R" -> go to the right node
        # "U" -> go to the parent node

        #key_observations
        # Both startValue and destValue will have some common ancestor nodes.
        # The nearest common ancestor node is called the LCA (Lowest Common Ancestor).
        # With the help of the LCA, we can find our shortest path.
        # From startValue to the LCA node, the path will consist of "U" since we will only be moving to parent nodes.
        # "L" and "R" will be used from the LCA node to destValue, depending on the direction required to reach the destination node.

        #Approach 1
        # First, find the LCA node.
        # Trace the path from startValue to the LCA and from the LCA to destValue.
        # Add "U" for the length of the path from startValue to the LCA to the result.
        # Then add the path from the LCA to destValue to the result.
        # Return the result.

        #Approach 2 (easier)
        # Trace the path from the root to startValue and from the root to destValue.
        # Use a pointer to navigate both paths and move until they are same.
        # Add "U" for the remaining steps in the startValue path to the result.
        # Then add the remaining steps in the destValue path to the result.

        #Complexities for Both Approaches
        # Time Complexity: O(N)
            # As we are traversing the nodes a constant number of times.
        # Space Complexity: O(N)
            # Storing paths requires space proportional to the number of nodes.


        # # Approach 1
        # # finding the LCA node
        # LCA = self.findLCANode(root, startValue, destValue)

        # srcToLCA = [] 
        # LCAtoDest = []

        # # findIng path from startValue to LCA
        # self.findPath(LCA, startValue, srcToLCA) # O(N)

        # # finding path from destValue to LCA
        # self.findPath(LCA, destValue, LCAtoDest) # O(N)

        # result = "U" * len(srcToLCA)
        # result += "".join(LCAtoDest)

        # return result


        # Approach 2
        srcToRoot = []
        rootToDest = []

        self.findPath(root, startValue, srcToRoot) # O(N)
        self.findPath(root, destValue, rootToDest) # O(N)

        pointer = 0

        while pointer < len(srcToRoot) and pointer < len(rootToDest) and srcToRoot[pointer] == rootToDest[pointer]:
            pointer += 1
        
        srcToRoot = srcToRoot[pointer:]
        result = "U" * len(srcToRoot)

        for i in range(pointer, len(rootToDest)):
            result += rootToDest[i]

        return result


    