# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/description/?envType=daily-question&envId=2024-06-24
# $ - Easy, $$ - Medium, $$$ - Hard

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        # Google

        # $$$ -> Hard

        # Brute Force
        # You flip all the 0 bits to 1 bits of k window size using two loops
        # First loop iterating the array and nested loop iterating the k window

        # Optimized Approach
        # You maintain a flipCount for k window while iterating the list
        # And using the flipCount judge if the current value require a flip or not
        # don't forget to reduce the flipCount outside of the k window 

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