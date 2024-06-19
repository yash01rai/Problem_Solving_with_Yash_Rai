# https://leetcode.com/problems/patching-array/?envType=daily-question&envId=2024-06-16

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        # dry run to get more understanding

        patch_count = 0
        maxReach = 0
        i = 0

        while maxReach < n:

            # we are able to get to the current number
            if i < len(nums) and maxReach + 1 >= nums[i]:
                maxReach += nums[i]
                i += 1
            else:
                # patching will result in maxReach
                maxReach += (maxReach + 1) # we patch the number that we aren't able to reach
                patch_count += 1 # increasing the patch count

                # patch make sure that we reach all the numbers till maxReach
        
        return patch_count
