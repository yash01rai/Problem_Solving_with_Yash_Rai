class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        # thinkkk
        # first what letters can be made
        # dictionary to maintain freq

        # take/not-take
        # take only if we have enough words
        # take possible function


        # choosing the letters to be made for the highest score
        # chosing the max score
        
        # result = 0
        n = len(words)

        dt = defaultdict(int)

        for letter in letters:
            dt[letter] += 1

        def checkWordPossibleTrack(word):
            
            result = True
            for x in word:
                dt[x] -= 1

                if dt[x] < 0:
                    result = False
            
            return result
        
        def wordPossiblBackTrack(word):
            for x in word:
                dt[x] += 1

        
        def getScore(word):
            result = 0

            for x in word:
                result += score[ord(x) - ord('a')]
            
            return result


        def dfs(i):
            if i == n:
                return 0
            
            notTake = dfs(i + 1)

            take = 0
            # track
            if checkWordPossibleTrack(words[i]):
                take = getScore(words[i]) + dfs(i + 1)
            
            # backtrack
            wordPossiblBackTrack(words[i])

            return max(notTake, take)
            
        return dfs(0)
