# https://leetcode.com/problems/most-beautiful-item-for-each-query?envType=daily-question&envId=2024-11-12

class Solution:
    def bSearch(self, items, price):
        l = 0
        r = len(items) - 1

        max_beauty = 0
        while l <= r:
            mid = l + (r - l) // 2

            if items[mid][0] > price:
                r = mid - 1

            else:
                max_beauty = max(max_beauty, items[mid][1])
                l = mid + 1
        
        return max_beauty


    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:


        # binary search?
        # stack?
        # NO to graph

        # 2 max till 1
        # 4 max till 2
        # 5 max till 4
        # 6 max till 6


        #Understanding
        # We are given a list of items where each item has a price and a beauty value. 
        # For each query, we need to find the maximum beauty of an item whose price is less than or equal to the query price.
        # If no item meets the price condition, the answer for that query should be 0.

        #key_observations
        # Sorting the items by price allows us to efficiently search for the maximum beauty up to any query price.
        # By using binary search, we can quickly find the highest beauty value for items within the query price range.
        # To facilitate binary search, we pre-process the items list by modifying each item's beauty to be the maximum beauty encountered up to that price.

        #Approach
        # 1. **Sort Items**: Sort `items` by price to allow efficient binary searching.
        # 2. **Pre-process Beauties**: Iterate through the sorted `items` to update each item’s beauty value with the maximum beauty seen so far.
        # 3. **Binary Search**: For each query, perform a binary search to find the maximum beauty for items with prices up to the query value.
        # 4. **Store Results**: Collect results for each query based on the binary search output.

        #concepts_used
        # Sorting : To arrange items by price.
        # Binary Search : To efficiently find the highest beauty up to a given price.
        # Dynamic Pre-processing : Modify the items list to track cumulative maximum beauties for faster querying.

        #complexities
        # Time Complexity : O(n log n + m log n)  
            # Sorting items takes O(n log n) and each query involves a binary search, adding O(m log n).
        # Space Complexity : O(n)  
            # For the pre-processed `items` list and result array.



        n = len(items)
        m = len(queries)

        items.sort()

        max_beauty = 0
        for i in range(n):
            max_beauty = max(max_beauty, items[i][1])
            items[i][1] = max_beauty


        result = [0] * m
        for j in range(m):
            result[j] = self.bSearch(items, queries[j])

        return result
