class Solution:
    def specialArray(self, nums: List[int]) -> int:
        N = len(nums)
        
        freq = [0] * (N + 1)
        for num in nums:
            freq[min(N, num)] += 1
        
        num_greater_than_or_equal = 0

        # traversing through freq list
        # going right to left make sure that current value will always have the count till
        # the current num and greater
        # as soon we encounter a number which matches our count we return the number
        for i in range(N, 0, -1):
            num_greater_than_or_equal += freq[i]
            if i == num_greater_than_or_equal:
                return i
        
        return -1