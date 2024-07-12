# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/?envType=daily-question&envId=2024-07-11

class Solution:
    def reverseParentheses(self, s: str) -> str:

        #Topics 
        # Stack, String

        #Understanding
        # In a given string, we need to reverse the substrings between the parentheses, starting from the innermost one.
        # The result should be returned without the parentheses.

        #key_observations
        # As we need to process chunks of the string between the parentheses starting from the innermost ones, this can be achieved using a stack.
        # Using a stack, we can process the innermost brackets while still keeping track of the outer brackets to be processed further.

        # Approach
        # Use two stacks.
        # Create a stack.
        # Iterate through the string.
        # Add the current character to the stack if it is not a closing parenthesis ")".
        # If the character is ")", do the following:
            # Create a reverseStack.
            # Add the popped elements from the stack to the reverseStack until you find an opening parenthesis "(", using a while loop.
            # Pop the opening parenthesis and extend the stack with the elements from the reverseStack.
        # Join the stack values and return the result.

        # Complexities
        # Time Complexity : O(N)
            # Because each character is processed a constant number of times.
        # Space Complexity : O(N)
            # For the stack storage.


        stack = []

        for char in s:
            
            if char == ")":
                reverseStack = []
                
                while stack[-1] != "(":
                    reverseStack.append(stack.pop())
                
                stack.pop()
                stack += reverseStack
            
            else:
                stack.append(char)
        
        result = "".join(stack)
        
        return result

        