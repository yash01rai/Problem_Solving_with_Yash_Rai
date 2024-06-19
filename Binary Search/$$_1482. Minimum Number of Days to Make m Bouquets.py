# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/?envType=daily-question&envId=2024-06-19

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        n = len(bloomDay)

        if m * k > n:
            return -1

        def isBouquet(days, k):
            result = 0 
            flowers = 0

            # adjaceny?
            for curr_day in bloomDay:
                if curr_day <= days:
                    flowers += 1
                else:
                    result += (flowers // k)
                    flowers = 0

            if flowers > 0:
                result += (flowers // k)

            return result >= m

        # iterate for every value of m?
        low = 1
        high = max(bloomDay)

        # it should be less than only when you are setting high on mid everytime
        # as you are trying to find the minimum days to make "m" bouquet
        while low < high:

            mid = (low + high) // 2

            if isBouquet(mid, k):
                high = mid
            else:
                low = mid + 1

        return low

        # when I'm trying to solve the question 
        # it want me to do certain things to solve it
        # basically as I encounter problems it led me towards the solution