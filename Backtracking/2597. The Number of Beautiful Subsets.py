class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        n = len(nums)
        def countBeautifulSubsets(nums, diff, freq, i):
            if i == n:
                return 1

            # not-taking
            total_count = countBeautifulSubsets(nums, diff, freq, i + 1)
            
            #taking if diff minus current value don't already exist

                freq[nums[i]] += 1
                total_count += countBeautifulSubsets(nums, diff, freq, i + 1)
                freq[nums[i]] -= 1

                if freq[nums[i]] == 0:
                    del freq[nums[i]]
            
            return total_count
        
        freqMap = defaultdict(int)
        nums.sort()

        return countBeautifulSubsets(nums, k, freqMap, 0) - 1


        