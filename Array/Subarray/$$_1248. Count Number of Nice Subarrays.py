# https://leetcode.com/problems/count-number-of-nice-subarrays/description/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        dt = defaultdict(int)
        dt[0] = 1

        result = 0
        odds = 0
        for num in nums:
            if num % 2 != 0:
                odds += 1

            if odds - k in dt:
                result += dt[odds - k]
            
            dt[odds] += 1
        
        return result