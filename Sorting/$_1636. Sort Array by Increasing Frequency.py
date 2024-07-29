# https://leetcode.com/problems/sort-array-by-increasing-frequency/description/?envType=daily-question&envId=2024-07-23

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        #Understanding
        # We need to sort the array under certain criteria:
        # 1. In increasing order based on the frequency.
        # 2. In decreasing order for the same frequency.

        # Approach (Python)
        # 1. Get the frequency of elements in the `nums` array.
        # 2. Utilize in-built sorting, where you define an anonymous lambda function.
        # 3. In the lambda function, taking `x` as an argument for `nums` elements:
            # Define the frequency of `x` as the first criteria.
            # Use `-x` as the second criteria for sorting in decreasing order.
        # 4. Return the sorted array.


        #Complexities
        # Time: O(nlogn)
        # Space: O(n)

        # optimized
        freq = Counter(nums)
        return sorted(nums, key= lambda x: (freq[x], -x))

        
        
        # brute force
        # dictionary to maintain num frequency
        dt = defaultdict(int)
        minHeap = []

        for num in nums:
            dt[num] += 1
        
        # minHeap to sort the frequency in non-decreasing order
        for k, v in dt.items():
            heappush(minHeap, (v, k))
        
        result = []

        # heap pop to generate the esult
        while minHeap:
            # sub array to maintain and sort the duplicates in reverse order 
            subArray = []
            
            # initial pop
            keyValue = heappop(minHeap)

            subArray.append(keyValue)
            # while there is a duplicate
            while minHeap and minHeap[0][0] == keyValue[0]:
                subArray.append(heappop(minHeap))

            # finaly updating the result using sub array
            while subArray:
                value, key = subArray.pop()

                curr = [key] * value
                result += curr

        return result