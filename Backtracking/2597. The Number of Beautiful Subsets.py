class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        # misout on the understanding part
        n = len(nums)
        def countBeautifulSubsets(nums, diff, freq, i):
            if i == n:
                return 1

            total_count = countBeautifulSubsets(nums, diff, freq, i + 1)

            if nums[i] - diff not in freq: # checking if there is value after taking out the diff already exists

                freq[nums[i]] += 1
                total_count += countBeautifulSubsets(nums, diff, freq, i + 1)
                freq[nums[i]] -= 1

                if freq[nums[i]] == 0:
                    del freq[nums[i]]
            
            return total_count
        
        freqMap = defaultdict(int)
        nums.sort()

        return countBeautifulSubsets(nums, k, freqMap, 0) - 1


        