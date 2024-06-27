# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/description/?envType=daily-question&envId=2024-06-24
# $ - Easy, $$ - Medium, $$$ - Hard

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        # Google

        n = len(nums)
        flips = 0

        flipCountForPasti = 0
        isFlipped = [False] * n

        for i in range(n):
            if i >= k and isFlipped[i - k] == True:
                flipCountForPasti -= 1
            
            # flipCountForPasti 3 nums[i] 1 -> 0 1 0 -> + 1 flip to make it work
            # flipCountForPasti 4 nums[i] 0 -> 1 0 1 0 -> + 1 flip to make it work
            if flipCountForPasti % 2 == nums[i]:
                # 0 has even flipCountForPasti, will result in 0 value
                # 1 has odd flipCountForPasti, will result in 0 value again
                # both the cases we have to flip again from the current value to end of the window
                # to get the current index value be 1
                
                if i + k > n:
                    return -1

                flipCountForPasti += 1
                flips += 1

                isFlipped[i] = True

        
        return flips