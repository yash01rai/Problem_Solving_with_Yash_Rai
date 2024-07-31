# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/?envType=daily-question&envId=2024-07-30

class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        # Understanding
        # We have a string that only contains 'a' and 'b'.
        # Our task is to return the number of deletions needed to make the string balanced.
        # A balanced string is one that does not contain "ba" in contiguous order.

        #key_observations
        # To achieve a balanced string, we can remove all the 'b's that come just before an 'a'.
        # This can be done with the help of a stack.
        # With the help of a stack, we can keep track of previous value incase deletion is required.

        #Approach
        # 1. Initialize a result variable to store the number of deletions and a stack to keep track of previous values in order.
        # 2. Iterate through the string:
            # If the stack is not empty, the top value of the stack is 'b', and the current character is 'a', 
                # Add 1 to the result, and pop the stack, representing the deletion of the character.
            # Else, append the current character to the stack.

        #Complexities
        # Time: O(n)
            # Visiting each character once.
        # Space: O(n)
            # The stack can store up to n characters from the string.


        result = 0
        stack = []

        for char in s:
            if stack and stack[-1] == "b" and char == "a":
                result += 1
                stack.pop()
            else:
                stack.append(char) 
        
        return result