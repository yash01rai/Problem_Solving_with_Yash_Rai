class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        # 15 // 4, 15 % 4
        # 3 , 3 -> 6
        # 1, 2 -> 3

        # Understanding
        # We are given a number of filled bottles (`numBottles`), and we can get more filled bottles in exchange for empty bottles.
        # The goal is to return the maximum number of water bottles you can drink.

        # Key Observations
        # When you have `numExchange` number of empty bottles, you can exchange them for 1 full bottle.
        # Keep consuming the bottles and then exchange the empty bottles to get more bottles.
        # Repeating the process will ensure that you'll get the maximum number of water bottles you can drink.

        # Approach
        # Keep a count of total bottles consumed.
        # Track the extra bottles that can't be exchanged at the moment.
        # Consume the bottles and exchange the empty bottles for full bottles at the `numExchange` rate.
        # Add the new bottles that can be consumed to the total count.
        # Add the extra bottles to the new bottles for further consumption.
        # Repeat the process until you don't have enough empty bottles to exchange.
        # Return the total count of bottles consumed.

        # Complexities
        # **Time complexity**: O(logN)
        # As we divide full bottles by `numExchange` at each iteration.
        # **Space complexity**: O(1)


        totalBottles = 0
        totalBottles += numBottles

        while numBottles >= numExchange:

            remainingBottles = numBottles % numExchange

            numBottles //= numExchange
            totalBottles += numBottles

            numBottles += remainingBottles
            
        return totalBottles