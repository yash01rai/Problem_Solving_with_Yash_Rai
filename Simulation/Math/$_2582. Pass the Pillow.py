# https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        # % will give me the postion
        # but how to get the direction ?

        # Understanding
        # A pillow is being passed from 1 to n people, and when it reaches the end, it is passed back.
        # Passing is done every second for the given time.
        # We need to return the person holding the pillow after the given time.

        # Key Observation
        # Initially, the first person is holding the pillow, so reaching the last person would take n - 1 seconds.
        # As we are going back and forth with the pillow, even rounds would mean the forward direction, and odd rounds would mean the backward direction.
        # The pillow position can be identified by the remaining time after completing full rounds.

        # Approach
        # Calculate the full rounds that can be taken with the given time.
        # The position can be determined based on the remaining time.
        # The forward and backward direction would be decided by the number of full rounds after the given time.
        # Return the position


        rounds = time // (n - 1)
        position =  time % (n - 1)

        print(rounds)
        print(position)

        if rounds % 2 == 0:
            return position + 1 # As we start with the 1 person already holding the pillow
        else:
            return n - position