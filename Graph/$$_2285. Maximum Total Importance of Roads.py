# https://leetcode.com/problems/maximum-total-importance-of-roads/
# $$ -> Medium

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        # how can I make sure that the right value assigned to get the maximum importance

        # assigning maximum value to the maximum adjcent cities where road is connecting

        # 𝐔𝐧𝐝𝐞𝐫𝐬𝐭𝐚𝐧𝐝𝐢𝐧𝐠

        # We have roads between cities numbered from 0 to n - 1, and we need to assign each city a value from 1 to n in such a way that results in maximum importance.
        # The importance of a road is defined as the sum of the values of the two cities it connects.
        # If you observe, this is a graph problem, and assigning greater values to cities with a larger number of connections (indegree) would result in maximum total importance.



        # Approach

        # Calculate the indegree of each city.
        # Sort the cities by their indegree in non-decreasing order.
        # As we need to assign the value from 1 to n.
        # While iterating over the sorted cities, multiply the assigned value (index + 1) by the indegree of the current city and add it to the result
        # As the indegree is sorted, the (index + 1) value would assign from lowest to greatest
        # As the indegree is sorted, the (index + 1) value will be assigned from lowest to highest.
        # return the result



        indegree = [0] * n
        for u, v in roads:
            indegree[u - 1] += 1
            indegree[v - 1] += 1

        indegree.sort()
        result = 0
        for i in range(n):
            result += (indegree[i] * (i + 1))

        return result


        #####################

        # Brute force
        importance = []
        for city, adjCities in adjList.items():
            importance.append((len(adjCities), city))

        importance.sort(key= lambda x: (x[0], x[1]))
        cityImportance = {}
        count = n
        while importance:
            cityImportance[importance.pop()[1]] = count
            count -= 1
        
        result = 0

        for u, v in roads:
            result += (cityImportance[u] + cityImportance[v])

        return result