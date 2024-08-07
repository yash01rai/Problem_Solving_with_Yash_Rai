# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/?envType=daily-question&envId=2024-08-06

class Solution:
    def minimumPushes(self, word: str) -> int:
        
        # brute
        # charCount = Counter(word)
        # sortedWord = sorted(word, key=lambda x: -charCount[x])

        # result = 0
        # wordSet = set()
        # for char in sortedWord:
        #     if char not in wordSet:
        #         times = (len(wordSet) // 8) + 1
        #         wordSet.add(char)
        #         print(char, times)
        #         result += charCount[char] * times

        # return result


        #Understanding
        # We need to find the minimum number of presses required on a telephone keypad to type a given word.
        # Each key on the telephone is mapped to a set of distinct lowercase English letters.
        # To get the desired character, we need to press its corresponding key a certain number of times. 
            # For example, if a key consists of "a", "b", "c", pressing it 3 times yields "c".
        # The goal is to map the characters to the keys such that the total number of presses is minimized.

        #key_observations
        # Characters placed at the start of the keys require fewer presses than those placed later.
        # Mapping the most frequently used characters to the start of the keys results in fewer presses overall.
        # Since there are only 8 keys (2 to 9) with characters, we can't place every character at the start. 
        # After placing the 8 most frequent characters at the start, we place other characters in descending order of frequency across the keys.
        # We repeat this process until all characters are assigned to keys.
        # Based on frequency and key position, we calculate the total number of presses needed to type the word.

        #Approach
        # 1. Count the frequency of each character in the word.
        # 2. Sort the characters by frequency in descending order.
        # 3. Maintain the unique count to know in which key the character is at
        # 4. Calculate the number of presses needed to type the character with the help of unique count
        # 5. Add the product of frequency and presses to the result and increase the unique count
        # 6. At the end return the result

        #Complexities
        # Time: O(n log n) for sorting the characters by frequency.
        # Space: O(n) for storing character frequencies.

        #Topics
        # Array, Sorting, Frequency Counting

        #Topics
        # Hash Table, String, Greedy, Sorting, Counting


        # Count the frequency of each character in the word
        charCount = Counter(word)
        # Sort the characters by their frequency in descending order
        sortedChars = sorted(charCount.items(), key=lambda x: -x[1])
        
        result = 0
        unique_count = 0
        
        for char, count in sortedChars:
            pushes = (unique_count // 8) + 1
            result += count * pushes
            unique_count += 1
        
        return result