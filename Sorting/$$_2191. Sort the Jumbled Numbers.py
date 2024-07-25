# https://leetcode.com/problems/sort-the-jumbled-numbers/?envType=daily-question&envId=2024-07-24
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        #Understanding
        # Given a mapping and a list of numbers (nums), we need to sort the numbers according to their mapped values and return the sorted list.
        # Each digit in the numbers list has a corresponding mapped value, i.e., mapping[digit].

        #key_observations
        # Sorting needs to be done based on the mapped value, but the original order should be maintained for numbers with the same mapped value.
        # Example: mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6], nums = [991, 338, 38]. Here, 338 and 38 have mapped values 007 and 07, respectively. The order will remain the same, with 338 coming before 38.
        # Converting the number to its respective mapped value can be done using strings or mathematical operations.

        #Approach
        # 1. Initialize `converted_values` as an empty array to store respective values and their index for further sorting.
        # 2. Iterate through the `nums` array, converting each value based on the mapping and storing the result along with its index in `converted_values`.
        # 3. If the number is zero, append its mapped value and index to `converted_values` and continue.
        # 4. For non-zero numbers, use place value to convert the number while iterating over its digits:
            # Get the last digit as `map_key` and multiply the mapped value by the place value, adding the previous mapped value.
            # Update the place value and the temporary value.
            # Repeat until all digits are converted.
        # 5. Add the (new value, index) to the `converted_values` list.
        # 6. Sort `converted_values`.
        # 7. Using the indexes in `converted_values`, generate the sorted result in original values.

        #Complexities
        # Time Complexity: O(n log n)
            # Mapping each number is O(1) because the number of digits is at most 9 (a constant).
            # Iterating through all n numbers and mapping them is O(n) × O(1) = O(n).
            # Sorting takes O(n log n).
        # Space Complexity: O(n)
            # Storing n converted values.

        #Topics
        # Array, Sorting


        converted_values = []
        for i in range(len(nums)):
            mapping_value = 0
            temp = nums[i]

            if temp == 0:
                converted_values.append((mapping[0], i))
                continue
                
            place = 1
            while temp > 0:
                map_key = temp % 10
                mapping_value = place * mapping[map_key] + mapping_value
                place *= 10
                temp //= 10
            
            converted_values.append((mapping_value, i))

        converted_values.sort()

        return [nums[val[1]] for val in converted_values]