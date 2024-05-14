# Find the pairs which sum is equal to given target in a sorted array

class Solution:
    def pairSumToTarget(self, nums, target):

        # nums = [1, 2, 3, 4, 6, 7, 8, 9, 10]
        # target = 12

        # brute force
        output = []
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    output.append([nums[i], nums[j]])

        print(output)

        # optimized solutions with speed
        visited = set()
        result = []
        for num in nums:
            if abs(target - num) in visited:
                result.append([abs(target - num), num])
            
            visited.add(num)
            
        print("result", result)

        # two pointer optimized solution with speed and space
        i = 0
        j = n - 1
        resultT = []
        while i < j:
            if nums[i] + nums[j] == target:
                resultT.append([nums[i], nums[j]])
                i += 1
                j -= 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
            
        print("3", resultT)

# Create an instance of the Solution class
solution_instance = Solution()

# Call the pairSumToTarget function using the instance
solution_instance.pairSumToTarget([1, 2, 3, 4], 5)
        
