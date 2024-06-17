# https://leetcode.com/problems/ipo/?envType=daily-question&envId=2024-06-15

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        # two heap pattern? -> Greedy -> peeking the best things first

        # Approach
        # We want the maximize the capital which lead to picking k largest profits
        # but we have the capital constraint which only let us pick the project which is lower or equal 
        # to our current capital
        # sorting the capital on the base in increasing order will make sure that we pick the smaller values
        # that can be picked on the basis of our current capital
        # And as soon as we have collected the valid projects
        # we select the max profit project out of them not breaking the k mark
        # as soon as our current cap reach the desired capital needed for current project
        # we break and start picking the projects in our reach
        # we repeat this process until we reach the end of the list or k projects picked


        capital_profit = [(cap, pro) for cap, pro in zip(capital, profits)]
        # sorting capital in increasing order
        capital_sort_profit = sorted(capital_profit, key=lambda x: (x[0], x[1]))

        max_heap = []

        curr_capital = w
        # iterating through capital profit list
        for cap, pro in capital_sort_profit:
            
            # while current capital is not enough for current project we get the maximum k profits
            while cap > curr_capital and max_heap:
                curr_capital += -heappop(max_heap)
                k -= 1

            # we break if we are not able to achieve the desired capital or we are done picking k projects
            if curr_capital < cap or k == 0:
                break

            # adding the projects profits achievable through out current capital to max heap 
            heappush(max_heap, -pro)
        
        # we take more profits if there are still k remaining projects and also max heap have the projects to provide
        while k > 0 and max_heap:
            curr_capital += -heappop(max_heap)
            k -= 1
        
        return curr_capital
            



        # not efficient, cause TLE
        # dfs take or not-take
        n = len(profits)
        dp = {}
        def dfs(i, cap, k):
            
            if (i, cap, k) not in dp:
                if i == n or k == 0:
                    return cap
                
                left = dfs(i + 1, cap + profits[i], k - 1) if cap >= capital[i] and k > 0 else 0
                right = dfs(i + 1, cap, k)
                
                dp[(i, cap, k)] = max(left, right)
            
            return dp[(i, cap, k)]

        return dfs(0, w, k)

    