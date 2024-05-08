class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        

        # memoization dp solution

        # only caching data which is required 
        prevDice = [0] * (target + 1)
        mod = (10 ** 9) + 7

        prevDice[0] = 1

        # Starting from single DICE till n dices
        for dice in range(1, n + 1):
            currDice = [0] * (target + 1)

            # Starting with 1 till the target
            for t in range(1, target + 1):
                ways = 0

                # Checking for all the faces starting from 1
                for faceVal in range(1, k + 1):
                    if t - faceVal >= 0:
                        ways += prevDice[t - faceVal] % mod
                
                currDice[t] = ways

            # replacing prevDice with curr
            prevDice = currDice
        return currDice[target] % mod


        # top down solutions
        def dfs(numDice, k, target):
            if target == 0 and numDice == 0:
                return 1
            
            if numDice == 0 or target <= 0:
                return 0

            if dp[numDice][target] == "$":
                ways = 0

                for faceVal in range(1, k + 1):
                    ways = ways + dfs(numDice - 1, k, target - faceVal)

                dp[numDice][target] = ways % mod
            
            return dp[numDice][target]
        
        return dfs(n, k, target)

        