# https://leetcode.com/problems/crawler-log-folder/description/?envType=daily-question&envId=2024-07-10

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        #Understanding
        # In a file system, after a given set of operations, we need to return the minimum number of operations required to go back to the main folder.
        
        # Key Observations
        # Based on the operations, we can define the depth of the folder at any given time.
        # We can only reach a certain folder by following a unique and continuous path.
        # The stack property of Last-In-First-Out (LIFO) would be helpful as per the above observation.

        # Approach 1
        # Create a stack.
        # Iterate through the logs.
        # Whenever we encounter a folder name operation, we add it to our stack.
        # When we encounter a move to the parent folder operation, we pop the stack.
        # For the "./" operation, we don't do anything.
        # Return the length of the stack as the answer.

        # Complexities 1
        # Time Complexity: O(N)
            # Visiting each log one time.
        # Space Complexity: O(N)
            # Use of the stack can extend to N space.

        # Approach 2 (optimized)
        # Instead of a stack, maintain a depth count.
        # Replace pop and append operations with decreasing and increasing the depth count, respectively.
        # Return the depth count.

        # Complexities 2
        # Time Complexity: O(N)
            # Visiting each log one time.
        # Space Complexity: O(1)
            # Constant space is used.
        
        # stack = []
        depth = 0
        for log in logs:
            if depth > 0 and log == "../":
                # stack.pop()
                depth -= 1
            elif log != "./" and log != "../":
                # stack.append(log)
                depth += 1
        
        return depth
