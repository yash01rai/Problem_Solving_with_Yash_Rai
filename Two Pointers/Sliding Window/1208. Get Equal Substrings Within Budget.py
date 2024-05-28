class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        # maintaing a window as we want to find the max substring (intuition)
        # where we increase the right pointer and add the cost until it exceeds the maxCost
        # we calculate the max length of substring
        # if cost exceeds we move the left pointer and shrink the window
        
        
        n = len(s)
        left = 0

        result = 0
        cost = 0
        for right in range(n):
            cost += abs(ord(s[right]) - ord(t[right]))

            if cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            else:
                result = max(result, right - left + 1)
        
        return result