class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        # what is possible
        last_day = days[-1]
        dp = [0] * (last_day + 1)
        travel_days = set(days)

        for i in range(1, last_day + 1):
            if i not in travel_days:
                dp[i] = dp[i - 1]  # If not traveling on day i, cost is same as previous day
            else:
                # Calculate the cost for each type of ticket
                one_day_cost = dp[max(0, i - 1)] + costs[0]
                seven_day_cost = dp[max(0, i - 7)] + costs[1]
                thirty_day_cost = dp[max(0, i - 30)] + costs[2]

                # Choose the minimum cost among the available options
                dp[i] = min(one_day_cost, seven_day_cost, thirty_day_cost)

        return dp[last_day]

        # time: O(days)
        
        # bottom up
        n = len(days)
        dp = [0] * len(days)
        dp[0] = min(costs)

        for i in range(1, n):
            
            day_1 = costs[0] + dp[i - 1]
            min_cost = day_1
            k = i - 1

            while k >= 0 and days[k] > days[i] - 7:
                k -= 1
            
            if k < 0:
                min_cost = min(min_cost, costs[1])
            else:
                min_cost = min(min_cost, costs[1] + dp[k])

            k = i - 1

            while k >= 0 and days[i] - 30 < days[k]:
                k -= 1
            
            if k < 0:
                min_cost = min(min_cost, costs[2])
            else:
                min_cost = min(min_cost, costs[2] + dp[k])
                

            dp[i] = min_cost
        
        return dp[n - 1]


        # top down
        dp = {}
        def dfs(i):

            if i in dp:
                return dp[i]

            if i == len(days):
                return 0

            min_cost = inf
            for j in range(len(costs)):
                
                if j == 0:  
                    min_cost = min(min_cost, costs[j] + dfs(i + 1))

                elif j == 1:

                    k = i
                    while k < len(days) and days[i] + 7 > days[k]:
                        k += 1

                    min_cost = min(min_cost, costs[j] + dfs(k))
                elif j == 2:

                    k = i
                    while k < len(days) and days[i] + 30 > days[k]:
                        k += 1

                    min_cost = min(min_cost, costs[j] + dfs(k))

            dp[i] = min_cost
            return dp[i]

        return dfs(0)