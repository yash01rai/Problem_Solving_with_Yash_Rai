# https://leetcode.com/problems/subarray-sums-divisible-by-k/?envType=daily-question&envId=2024-06-09
# similar leetcode 523

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        # as the requirement states that we want subarray sum which is divisible by k
        # maintain a prefix sum
        # store its remainder an encounter count and add that to result each time it found again
        # intiate the dictionary with { 0 : 1 }


        result = 0

        dt = defaultdict(int)
        dt[0] = 1

        prefSum = 0

        for i, n in enumerate(nums):
            prefSum += n

            r = prefSum % k
            if r in dt:
                result += dt[r]
            
            dt[r] += 1

        
        return result