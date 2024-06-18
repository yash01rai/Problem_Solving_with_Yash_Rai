# https://leetcode.com/problems/most-profit-assigning-work/?envType=daily-question&envId=2024-06-18

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        # approach 2
        # slightly better and more readable

        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        max_profit = 0
        result = 0
        j = 0
        
        for ability in worker:
            while j < len(jobs) and ability >= jobs[j][0]:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            result += max_profit
        
        return result

        # approach 1
        difficulty_profit = sorted(zip(difficulty, profit))
        worker.sort()

        max_profit = 0
        i = 0

        result = 0
        for d, p in difficulty_profit:

            while i < len(worker) and worker[i] < d:
                result += max_profit
                i += 1
            
            max_profit = max(max_profit, p)

            if i == len(worker):
                break
        
        while i < len(worker):
            result += max_profit
            i += 1
        
        return result