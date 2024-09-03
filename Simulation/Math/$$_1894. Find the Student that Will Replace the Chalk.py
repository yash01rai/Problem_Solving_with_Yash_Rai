# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/?envType=daily-question&envId=2024-09-02

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        #Understanding
        # We are given a list `chalk` where `chalk[i]` represents the amount of chalk required by the `i-th` student to solve a problem.
        # If we have `k` pieces of chalk, the teacher distributes chalk from student `0` to student `n-1`. 
        # And the chalk runs out, the student who cannot receive the required chalk will replace the chalk.
        # If some chalk remains after reaching the last student (`n-1`), the teacher starts again from student `0`, continuing this cycle until the chalk needs to be replaced.
        # Our task is to return the index of the student who ends up replacing the chalk.

        #key_observations
        # Simulating this process is possible but inefficient when the number of rounds is large.
        # Instead, we can calculate the total chalk consumption in one round by summing all elements in the `chalk` list.
        # This sum helps us determine how many complete rounds we can make before the chalk runs out, and we use this information to efficiently find the student who will replace the chalk.

        #Approach
        # 1. Iterate through the `chalk` list and calculate the total sum (`chalk_sum`) of chalk needed in one full round.
        # 2. Reduce `k` by the chalk requirement of each student (`chalk[i]`). If `k` becomes less than 0, return the current index `i`, as this student will replace the chalk.
        # 3. If the chalk does not run out within one full round (i.e., we finish the loop without `k < 0`), calculate the remaining chalk using `k % chalk_sum`.
        # 4. Iterate through the `chalk` list again with the remaining chalk. The first student where `chalk[i]` is greater than the remaining chalk will be the one who replaces the chalk, and we return their index.

        #Complexities
        # Time Complexity: O(n) 
            # for calculating the total sum of chalk and another O(n) for the second iteration.
        # Space Complexity: O(1) 
            # since we only use a few variables aside from the input list.

        n = len(chalk)
        chalk_sum = 0

        for i in range(n):
            chalk_sum += chalk[i]
            k -= chalk[i]

            if k < 0:
                return i
        
        remaining = k % chalk_sum

        for i in range(n):
            remaining -= chalk[i]

            if remaining < 0:
                return i