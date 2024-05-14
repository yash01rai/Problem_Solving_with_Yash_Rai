class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        # Write
        # 1. Understanding
        # 2. Observation
        # 3. DSA intuition

        # lower wage-to-quality ratios could potentially lead to a lower overall cost

        # Idea behind the approach
        # lower wage-to-quality ratios could potentially lead to a lower overall cost
        # sorting the rate in increasing order and the quality to calculate the answer
        
        # How sorting is helping us?
        # We know that the current rate in traversal would be the highest till now
        # it means accumalted qualities from k works would be calculate with that rate

        # Functioning of Heap
        # storing k and maintaing k works in maxHeap of quality
        # we have reached more than k works, now we remove the highest number of quality to reduce 
        # the total cost

        # And every time there are k works, we will calculate the minimum cost

        n = len(quality)
        total_cost = float("inf")

        wage_to_quality_ratio = []

        # Calculate wage-to-quality ratio for each worker
        for i in range(n):
            wage_to_quality_ratio.append((wage[i] / quality[i], quality[i]))

        # Sort workers based on their wage-to-quality ratio
        wage_to_quality_ratio.sort(key=lambda x: x[0])
        
        # Use a heap to keep track of the highest quality workers
        highest_quality_workers = []

        current_total_quality = 0
        # Iterate through workers
        for i in range(n):
            heapq.heappush(highest_quality_workers, -wage_to_quality_ratio[i][1])
            current_total_quality += wage_to_quality_ratio[i][1]

            # If we have more than k workers, 
            # remove the one with the highest quality
            if len(highest_quality_workers) > k:
                current_total_quality += heapq.heappop(highest_quality_workers)

            # If we have exactly k workers, 
            # calculate the total cost and update if it's the minimum
            if len(highest_quality_workers) == k:
                total_cost = min(
                    total_cost, current_total_quality * wage_to_quality_ratio[i][0]
                )

        return total_cost