class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # sorting and greedy was in my mind
        # but I read the constraints not correctly, if it can be solved in 10^4
        # it can better be solved O(n logn)

        people.sort()
        n = len(people)

        left = 0
        right = n - 1

        result = 0
        while left <= right:
            result += 1

            if left < right and people[left] + people[right] <= limit:
                left += 1
            
            right -= 1

        return result