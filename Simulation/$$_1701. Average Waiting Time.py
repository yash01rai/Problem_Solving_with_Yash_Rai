# https://leetcode.com/problems/average-waiting-time/?envType=daily-question&envId=2024-07-09

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        #Topics
        # Array, Simulation

        #Understanding
        # Given a sorted array on arrival times, we need to return the average wait time for a customer to receive their order.

        #key_observations
        # The arrival time of the customer and the chef's availability play a crucial role here.
        # The chef's availability is the priority, even if the customer has already arrived, because the chef can handle only one order at a time.
        # If the chef is available, the order will only be taken at the time of the customer's arrival.
        # For example, if the chef gets available at time 07 and the customer arrives at 05, the chef will only start working on the order after 07.

        #Approach
        # We maintain `currentTime` starting from the first customer's arrival time to track operations.
        # `totalWaitTime` is used to keep the sum of all the customers' wait times.
        # As we iterate through the list of customers, we calculate the `currentFinishTime` of the order.
        # Update `currentTime` if the arrival time of the customer is later than `currentTime`.
        # Subtracting the arrival time from `currentFinishTime` will give us the wait time of the current customer.
        # Add the wait time to `totalWaitTime`.
        # Update `currentTime` with the `currentFinishTime` of the customer's order.
        # Calculate and return the average wait time using `totalWaitTime`.

        #Complexities
        # Time Complexity : O(N)
            # As we are handling one order at a time.
        # Space Complexity : O(1)
            # Constant space is used.



        n = len(customers)

        currentTime = customers[0][0]
        totalWaitTime = 0

        for arrival, time in customers: 

            if currentTime < arrival:
                currentTime = arrival

            currentFinishTime = currentTime + time
            waitTime = currentFinishTime - arrival

            totalWaitTime += waitTime
            currentTime = currentFinishTime
        
        averageWaitTime = totalWaitTime / n

        return averageWaitTime
