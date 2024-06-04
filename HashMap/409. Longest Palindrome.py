# https://leetcode.com/problems/longest-palindrome/description/?envType=daily-question&envId=2024-06-04

class Solution:
    def longestPalindrome(self, s: str) -> int:

        dt = defaultdict(int)

        result = 0
        for char in s:
            dt[char] += 1
            if dt[char] % 2 == 0:
                result += 2
        
        for v in dt.values():
            if v % 2:
                result += 1
                break
        
        return result
    
        # don't forget to consider odd count of char as it can be made even after subtracting 1 