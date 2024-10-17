class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        #abcabcabc
        #aabbccabc
        #aabaccbcb

        #Understanding
        # We need to generate the longest possible happy string based on the given constraints.
        # The string should only contain the characters 'a', 'b', 'c' and must not have more than 2 consecutive occurrences of the same character.
        # Additionally, the number of occurrences of 'a', 'b', and 'c' should not exceed the values of `a`, `b`, and `c`, respectively.

        #key_observations
        # The largest count of a character should be used first to maximize the length of the string.
        # We must avoid placing the same character consecutively more than twice (e.g., "aaa").
        # We should greedily append the most frequent character unless it violates the rule, in which case we use the second most frequent.

        #Approach
        #1. Use a max heap to manage the counts of 'a', 'b', and 'c' in descending order.
        #2. Append the most frequent character unless it forms an invalid sequence.
        #3. If appending the most frequent character causes a violation (three consecutive occurrences), append the next most frequent character instead.
        #4. Continue this process, re-pushing characters with remaining counts back into the heap.
        #5. Stop when no more valid characters can be appended.

        #concept_used
        # Max Heap for keeping track of the most frequent characters.
        # Greedy approach to append the character with the highest remaining count.
        # Edge case handling to ensure no more than 2 consecutive characters are the same.

        #Complexities
        # Time Complexity: O((a + b + c) log 3)  
            # Inserting and removing from the heap takes O(log 3), and we do this for all characters.
        # Space Complexity: O(a + b + c)  
            # Storing the result string requires space proportional to the total number of characters.



        # Max heap to store counts of 'a', 'b', 'c'
        max_heap = []
        
        # Push the characters and their counts into the heap
        if a > 0:
            heappush(max_heap, (-a, 'a'))

        if b > 0:
            heappush(max_heap, (-b, 'b'))

        if c > 0:
            heappush(max_heap, (-c, 'c'))
        
        result = []
        while max_heap:
            count, letter = heappop(max_heap)  # Get the character with the most remaining count
            count = -count  # Since we store negative values for max heap functionality
            
            # Check if appending this letter would violate the rule (i.e., "aaa", "bbb", or "ccc")
            if len(result) >= 2 and result[-1] == letter and result[-2] == letter:
                # If no other character is available, return what we have so far
                if not max_heap:
                    return "".join(result)
                
                # Take the second most frequent character
                next_count, next_letter = heappop(max_heap)
                next_count = -next_count
                result.append(next_letter)
                next_count -= 1
                
                # Push back the second most frequent character if it still has remaining count
                if next_count > 0:
                    heappush(max_heap, (-next_count, next_letter))
                
                # Re-push the original letter back into the heap
                heappush(max_heap, (-count, letter))
            else:
                # If no rule is violated, append the letter and decrease its count
                result.append(letter)
                count -= 1
                
                # If there's still count left, push the letter back into the heap
                if count > 0:
                    heappush(max_heap, (-count, letter))
        
        return "".join(result)
