# https://leetcode.com/problems/sentence-similarity-iii/description/?envType=daily-question&envId=2024-10-06

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        

        #Understanding
        # We are given two sentences, and we need to determine if they are similar.
        # A sentence is considered similar if we can insert a contiguous sub-sentence into one sentence to make it identical to the other.

        #key_observations
        # We can insert a single sub-sentence either at the beginning, in the middle, or at the end of the other sentence.
        # We are not allowed to change existing words, only insert a sub-sentence.
        # The goal is to remove common words from the left and right of both sentences. Whatever remains is the part that could be inserted.
        # If after removing the common words, one of the deques is empty, the sentences are similar.

        #Approach
        # 1. Initialize two deques, each containing the words from the respective sentences.
        # 2. Pop the common contiguous words from the left of both deques.
        # 3. Repeat the same process from the right of both deques.
        # 4. If one of the deques becomes empty after these operations, the sentences are similar.
        # 5. If both deques still contain words, the sentences are not similar.

        #concept_Used
        # Deques for efficient popping from both ends.
        # String comparison.

        #Complexities
        # Time Complexity: O(n)
            # where n is the length of the shorter sentence. We traverse the words in both sentences from both ends.
        # Space Complexity: O(n) 
            #for storing the words of the sentences in deques.

        q1 = deque(sentence1.split(" "))
        q2 = deque(sentence2.split(" "))

        while q1 and q2 and q1[0] == q2[0]:
            q1.popleft()
            q2.popleft()

        while q1 and q2 and q1[-1] == q2[-1]:
            q1.pop()
            q2.pop()

        return not q1 or not q2