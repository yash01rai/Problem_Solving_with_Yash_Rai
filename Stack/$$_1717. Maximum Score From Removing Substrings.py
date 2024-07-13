# https://leetcode.com/problems/maximum-score-from-removing-substrings/?envType=daily-question&envId=2024-07-12

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        # Topics
        # String, Stack, Greedy

        # Understanding
        # We have to remove "ab" and "ba" from a given string.
        # Both operations will give certain points.
        # We have to maximize the gained points.

        #key_observations
        # As we are removing a certain pair at a time, we can use a stack.
        # Using a stack, we can process the current pair as well as new pairs we encounter after the process.
        # To maximize the value, we should first process the higher value pair.

        # Approach
        # We'll first remove the higher value pair from the given string.
        # Create variables for the top pair, top score, bottom pair, and bottom score based on the x and y values.
        # Iterate through the string and add characters to the stack.
        # When you encounter the current value and the stack's top value forming the top pair:
        # Add the top score to the result and pop the stack.
        # Update the string value from the remaining stack and empty the stack for further use.
        # Now iterate through the new string and remove the bottom pair, as they give fewer or equal points.
        # Follow the same process as the top pair and replace the top pair and score with the bottom pair and score.
        # Return the result.

        # Complexities
        # Time complexity: O(N)
            # We iterate through a stack of size up to N only twice.
        # Space complexity : O(N)
            # Using two stacks of size up to N.

        
        result = 0

        # priortize bigger value
        top = "ba"
        top_score = y
        bot = "ab"
        bot_score = x

        if y < x:
            top = "ab"
            top_score = x
            bot = "ba"
            bot_score = y

        n = len(s)
        stack = []
 
        for i in range(n):
            if s[i] == top[1] and stack and stack[-1] == top[0]:
                result += top_score
                stack.pop()
            else:
                stack.append(s[i])
        
        s = ''.join(stack)    
        stack = []
        for i in range(len(s)):
            if s[i] == bot[1] and stack and stack[-1] == bot[0]:
                result += bot_score
                stack.pop()
            else:
                stack.append(s[i])
        
        return result
