# https://leetcode.com/problems/number-complement/description/?envType=daily-question&envId=2024-08-22

class Solution:
    def findComplement(self, num: int) -> int:
        
        # convert and flip the binary
        binary = ""
        while num:
            flip = 0 if num % 2 else 1
            binary = str(flip) + binary
            num //= 2

        # convert back to decimal
        place = 0
        result = 0
        for i in range(len(binary) - 1, -1, -1):

            if binary[i] == "1":
                result += (2 ** place)
            
            place += 1

        return result
