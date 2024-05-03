class Solution:
    def minSteps(self, n: int) -> int:
        
        # Approach: Prime factorization
        # Look for the pattern which here seems related to prime numbers
        # meaning prime value of n is n itself
        # or if split it's composite value p * q until you reach the composite prime
        # 9 => 3 * 3
        # 14 => 7 * 2 => (2) is used and now we know remaining is prime which need to added as it is
        # which mean breaking it further won't be possible that would get us the desired result
        # we have to account for each value

        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans

        # Memoization
        dp = {}
        def dfs(current, copy):

            if (current, copy) in dp:
                return dp[(current, copy)]

            if current == n:
                return 0

            if current > n:
                return inf

            copy_paste = 2 + dfs(current + current, current) 

            paste = inf
            if copy != 0:
                paste = 1 + dfs(current + copy, copy)

            dp[(current, copy)] =  min(copy_paste, paste) # copy is an operation itself
            return dp[(current, copy)]

        return dfs(1, 0) 