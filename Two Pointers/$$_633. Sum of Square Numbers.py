# https://leetcode.com/problems/sum-of-square-numbers/?envType=daily-question&envId=2024-06-17

class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        # binary search? -> linearly finding the solution will give TLE
        # inceasing the lower pointer
        # decreasing the higher pointer

        low = 0
        high = int(c ** 0.5)

        while low <= high:
            mid = low * low + high * high

            if mid > c:
                high -= 1
            elif mid < c:
                low += 1
            else:
                return True
        
        return False
        # utilize the whole time of the timer, take 5 mins more if still not solve
        # give your brain chance to think and let it lead you to the solution

        # 12
        # 1 1 = 2
        # 1 2 = 5
        # 2 2 = 8
        # 1 3 = 10
        # 2 3 = 15
        # 1 4 = 17
        # 3 3 = 18
        # 2 4 = 20
        # 3 4 = 25
        # 4 4 = 32
        
        
        