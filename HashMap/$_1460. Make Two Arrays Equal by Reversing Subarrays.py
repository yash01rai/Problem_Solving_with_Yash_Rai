# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/?envType=daily-question&envId=2024-08-03

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        #Understanding
        # Given two positive integer lists, target and arr.
        # We need to determine if arr match target by reversing arr non-empty subarrays any number of times.

        #key_observations
        # Reversing arr to match target is only possible if both arr and target contain the same integers with the same frequencies.
        # Therefore, simply determining if the frequencies of integers in both lists match will provide the desired result.

        #Approach
        # 1. Store the frequency of target integers in a dictionary called `targetCount`.
        # 2. Iterate over the list arr.
        # 3. For each integer in arr:
            # If the integer is in `targetCount` and its frequency is greater than 0, reduce the frequency by 1.
            # Otherwise, return False, as the integer might not be found or its count is incorrect.
        # 4. Return True if the iteration is completed without issues.

        #Complexities
        # Time: O(n)
            # Adding frequencies to the dictionary and iterating over arr both result in O(n) complexity.
        # Space: O(n)
            # Storing the frequencies of n integers requires O(n) space.

        #Topics
            # Array, Hash Table, Sorting


        targetCount = Counter(target)
        
        for num in arr:
            if num in targetCount and targetCount[num] > 0:
                targetCount[num] -= 1
            else:
                return False
        
        return True