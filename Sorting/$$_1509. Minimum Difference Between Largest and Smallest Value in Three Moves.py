# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/?envType=daily-question&envId=2024-07-03
# $$ - Medium

class Solution:
    def minDifference(self, nums: List[int]) -> int:

        # 𝐔𝐧𝐝𝐞𝐫𝐬𝐭𝐚𝐧𝐝𝐢𝐧𝐠
        # We need to change at most three values in the nums array so that the difference between the minimum and maximum values is minimized.

        # 𝐀𝐩𝐩𝐫𝐨𝐚𝐜𝐡
        # If you observe, you can see that we only require the maximum and minimum values from the array to solve this problem.
        # Since the other values are not important and we seek the minimum and maximum values, we sort the array.
        # As you can change at most three values, your task is to bring down the maximum value or increase the minimum value to get the minimum difference.
        # By changing up to three maximum values and three minimum values, you can achieve the minimum difference.

        # 𝐇𝐨𝐰 ?
        # [20, 75, 81, 82, 95] suppose you got this array after sorting
        # you can perform 4 kind of changes to achieve the minimum difference

        # 1. Changing all three max value
        # we get [20, 75, 75, 75, 75] -> 75 - 20 = 55

        # 2. Changing 2 max value and 1 min value
        # [75, 75, 81, 81, 81] -> 81 - 75 = 6

        # 3. 1 max value and 2 min value
        # [81, 81, 81, 82, 82] -> 82 - 81 = 1

        # 4. 3 min value
        # [82, 82, 82, 82, 95] -> 95 - 82 = 13

        # Minimum value would be the answer i.e. 1

        if len(nums) <= 3:
            return 0
            
        nums.sort()

        first_set = nums[-4] - nums[0]
        second_set = nums[-3] - nums[1]
        third_set = nums[-2] - nums[2]
        fourth_set = nums[-1] - nums[3]

        return min(first_set, second_set, third_set, fourth_set)

        

         