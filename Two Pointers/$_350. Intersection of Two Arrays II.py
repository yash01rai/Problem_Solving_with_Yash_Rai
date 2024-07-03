class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Understanding
        # We need to return the common elements between nums1 and nums2, including duplicate values.

        # Approach
        # First, we need lists to be in order, so we sort them.
        # Using two pointers, we move through both arrays.
        # When we encounter a larger value in one pointer, we move the pointer with the lower value one step ahead, and vice-versa.
        # If we encounter the same value in both pointers, we add that value to our result and move both pointers ahead.
        
        nums1.sort()
        nums2.sort()
        
        result = []
        p1 = 0
        p2 = 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1

            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        
        return result