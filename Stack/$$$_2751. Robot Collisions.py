# https://leetcode.com/problems/robot-collisions/description

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        #Topics
        # Array, Stack, Sorting, Simulation

        #Understanding
        # Given robots, based on position, health, and direction, eliminate robots and return the health of the remaining robots.
        # If two robots are moving towards each other:
        # The robot with lower health will be eliminated, and the robot with higher health will reduce by one.
        # Robots with the same health will both be eliminated.

        #key_observations
        # As we need to process two consecutive robots at a time, this can be done using a stack.
        # Using a stack ensures that we can process the current robot in relation to all previous robots.
        # Since the positions are jumbled, ensure to sort the robots for simulation.
        # Only the current robot moving to the left can collide with the previous robot moving to the right.
        # We need to keep track of robot positions as we need to return the health in the original order.

        #Approach
        # Create an indices array to keep track of robots and sort them based on the robots' positions.
        # Maintain a stack while iterating over robot indices.
        # Add right-moving robots to the stack.
        # If you encounter robots moving to the left:
        # While the stack has robots and the health of the current robot is greater than 0:
            # Pop the stack and check for collision criteria.
            # If the health of the top stack robot is greater than the current robot's health, set the current robot's health to 0 and push the top robot back to the stack after reducing its health by 1.
            # If the opposite is true, set the health of the top robot to 0 and reduce the health of the current robot by 1.
            # If the health of both robots is the same, set both their health values to 0.
        # Collect the surviving robots in the result and return the result.

        # Complexities
            # Time Complexity: O(n log n)
            # Space Complexity: O(n)



        # Optimized Approach
        n = len(positions)
        indices = [i for i in range(n)]
        stack = deque()
        result = []

        # Sort indices based on their positions
        indices.sort(key=lambda x: positions[x])

        for current_index in indices:

            # Add right-moving robots to the stack
            if directions[current_index] == "R":
                stack.append(current_index)

            else:

                while stack and healths[current_index] > 0:

                    # Pop the top robot from the stack for collision check
                    top_index = stack.pop()

                    if healths[top_index] > healths[current_index]:

                        # Top robot survives, current robot is destroyed
                        healths[top_index] -= 1
                        healths[current_index] = 0
                        stack.append(top_index)

                    elif healths[top_index] < healths[current_index]:

                        # Current robot survives, top robot is destroyed
                        healths[current_index] -= 1
                        healths[top_index] = 0

                    else:

                        # Both robots are destroyed
                        healths[current_index] = 0
                        healths[top_index] = 0

        # Collect surviving robots
        for index in range(n):
            if healths[index] > 0:
                result.append(healths[index])

        return result


        # Brute Force
        
        n = len(positions)
        roboSort = sorted([(positions[i], healths[i], directions[i], i) for i in range(n)], key=lambda x: (x[0], x[1]))
        
        roboStack = []

        for i in range(n):
            if roboStack and roboStack[-1][1] == "R" and roboSort[i][2] == "L":
                
                if roboStack[-1][0] > roboSort[i][1]:
                    roboPop = roboStack.pop()
                    roboStack.append((roboPop[0] - 1, roboPop[1], roboPop[2]))
                    
                elif roboStack[-1][0] < roboSort[i][1]:

                    currentHealth = roboSort[i][1]
                    direction = roboSort[i][2]
                    index = roboSort[i][3]
                    isEqual = False

                    while roboStack and roboStack[-1][1] == "R" and roboSort[i][2] == "L" and (roboStack[-1][0] <= currentHealth or roboStack[-1][0] >= currentHealth):
                        if roboStack[-1][0] < currentHealth:      
                            currentHealth -= 1
                            roboStack.pop()

                        elif roboStack[-1][0] > currentHealth:
                            currentHealth = roboStack[-1][0] - 1
                            direction = roboStack[-1][1]
                            index = roboStack[-1][2]
                            roboStack.pop()
                            break

                        else:
                            isEqual = True
                            roboStack.pop()
                            break
                        

                    if isEqual == False:
                        roboStack.append((currentHealth, direction, index))

                else:
                    roboStack.pop()


            else:
                roboStack.append((roboSort[i][1], roboSort[i][2], roboSort[i][3]))

        if len(roboStack) == n:
            return healths

        originalOrder = sorted([(roboStack[i][0], roboStack[i][2]) for i in range(len(roboStack))], key=lambda x: x[1])
        
        result = [originalOrder[i][0] for i in range(len(originalOrder))]
        return result

        # doing to many operations need to double check the flow
        # to many variables