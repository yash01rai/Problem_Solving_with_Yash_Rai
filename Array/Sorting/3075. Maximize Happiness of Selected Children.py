class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort(reverse=True)
        happinessDown = 0
        result = 0

        for h in happiness:
            if k == 0:
                break
            
            currentHappy = h - happinessDown
            result += currentHappy if currentHappy >= 0 else 0

            happinessDown += 1
            k -= 1
        
        return result