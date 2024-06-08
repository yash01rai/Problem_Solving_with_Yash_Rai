# https://leetcode.com/problems/continuous-subarray-sum/?envType=daily-question&envId=2024-06-08

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # maintain prefix sum 
        # storing it's remainder genrated by mod k in dictionary

        # if we encounter same remainder it means that in between there is a subarray
        # which divisible by k
        # as we'll be storing indexes in the hashmap we can check of subarray length
        # by subtracting stored index from current index

        # as in intial value of 0 and index -1
        # it is done incase there exist a single length value on the start which is divisible by k

        total = 0
        remainderMap = { 0: -1 }

        for i, n in enumerate(nums):
            total += n
            r = total % k 

            if r not in remainderMap:
                remainderMap[r] = i
            elif i - remainderMap[r] > 1:
                return True

        return False