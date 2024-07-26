class Solution:
    def mergeFunction(self, left, right):
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        merged += left[i:]
        merged += right[j:]

        return merged


    def mergeSort(self, arr):

        if len(arr) == 1:
            return arr

        mid = len(arr) // 2
        left_arr = self.mergeSort(arr[:mid])
        right_arr = self.mergeSort(arr[mid:])

        return self.mergeFunction(left_arr, right_arr)


    def sortArray(self, nums: List[int]) -> List[int]:

        #Understanding
        # We need to sort the given array in ascending order.

        #Approach (Merge Sort)
        # Pass the array to a recursive function where we find the midpoint of the array.
        # Based on the midpoint, we divide the array into two parts and call the recursion on each part.
        # Continue dividing the array until we reach subarrays of a single element or less, then return them.
        # Pass both halves to a merge function.

            # Merge Function:
            # Initialize two pointers, `i` and `j`, to iterate through both halves of the array.
            # If the `i` element in the left half is smaller, push it to the merged array and move the `i` pointer by +1.
            # Otherwise, push the `j` element from the right half to the merged array and move the `j` pointer by +1.
            # After exiting the loop, extend any remaining elements from the left or right half to the merged array.
            # Return the merged array from the merge function.

        # Return the merged array in the recursion.
        # At the end, the merge sort will return our sorted array as the result.

        #Complexities
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)

        
        return self.mergeSort(nums)
        
        # Use **Quick sort** for better space complexity