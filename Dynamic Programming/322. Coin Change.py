# https://leetcode.com/problems/coin-change/description/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Bottom Up
        dp = [inf] * (amount + 1) # will store minimum coins needed to certain amount
        dp[0] = 0 # 0 means no coins required

        for amt in range(1, amount + 1):
            for c in coins:
                    if amt - c >= 0:
                        # use current coin and get remaining val from dp vs the current amount in dp
                        dp[amt] = min(dp[amt - c] + 1,  dp[amt])
        
        return dp[amount] if dp[amount] != inf else -1

        # Top Down
        dp = {}
        def dfs(i, amt):

            if amt in dp:
                return dp[amt]

            if amt == amount:
                return 0
            
            if amt > amount or i == len(coins):
                return inf

            dp[amt] = min(1 + dfs(i, amt + coins[i]), dfs(i + 1, amt))
            return dp[amt]

        min_coins = dfs(0, 0)
        return min_coins if min_coins != inf else -1

        # Time - O(amt * n)
        # Space - O(amt)