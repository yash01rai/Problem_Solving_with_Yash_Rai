# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/?envType=daily-question&envId=2024-07-26

class Solution:
    def bfs(self, city, adjList, dt):

        totalCities = 0
        minHeap = []
        heappush(minHeap, (0, city))
        visited = set()

        while minHeap:
            curr_dist, curr_city = heappop(minHeap)

            if curr_city in visited:
                continue

            if curr_dist > dt:
                break
            
            visited.add(curr_city)
            
            if curr_city != city:
                totalCities += 1

            for neighbour, cd in adjList[curr_city]:
                if neighbour not in visited:
                    heappush(minHeap, (curr_dist + cd, neighbour))
        
        return totalCities

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        #Understanding
        # Given edges of bi-directional and weighted graph of cities [fromi, toi, weighti]
        # we have to return city with the lowest number of cities that are reachable through some path 
        # and whose distance is at most distanceThreshold

        #key_obsrevations 
        # all the weights are positive
        # as we are looking for reachable node with at most distanceThreshold, we need look shortest path for every city
        # reason -> 1 edge can take up more than distanceThreshold or 3 edges can be within distanceThreshold from different path reaching the same edge
        # All the above points are pointing to Dijkstra algorithm
        # End goal is not to get the shortest path but to get minimum number of reachable cities <= distanceThreshold
        # Also incase of same minimum cities return greatest number city

        #Approach
        # 1. First, build a graph for 0 to n - 1 cities.
        # 2. Maintain a minimum cities count and a result variable.
        # 3. Iterate through each city and get their valid number of reachable cities using Dijkstra's algorithm:
            # In Dijkstra's algorithm, maintain a `totalCities` count, already visited cities and a `minHeap` to process cities and the distance required to reach them
            # While `minHeap` is not empty:
                # Pop the minHeap to get the minimum distance and the city. If it is visited, skip it.
                # If the current distance exceeds `distanceThreshold`, break the loop.
                # Increase the count of `totalCities` if the current city is not the source city.
                # Add the neighboring cities to the `minHeap` if they are not already visited.
            # Return the total number of cities.
        # 4. Check if the number of cities is less than the minimum cities count, or equal to it and the city number is greater than the current result.
        # 5. Update the result and minimum cities count if the above condition matches.
        # 6. Return the result.

        #Complexities
        # Time Complexity
            # Building adjacency list: O(E), where E is the number of edges.
            # Dijkstra's algorithm: O((V + E) log ⁡V) for each city, where V is the number of vertices (cities).
            # Total for all cities: O(V * (V + E) log ⁡V)
        # Space Complexity
            # Adjacency list: O(V + E)
            # Min-Heap and other structures for Dijkstra: O(V)

        # Overall Complexity
            # Given that V = n, 
            # Time: O(n ^ 2 log ⁡n)
            # Space: O(n + E)

        adjList = {i : [] for i in range(n)}

        for u, v, w in edges:
            adjList[u].append((v, w))
            adjList[v].append((u, w))
        
        minCities = inf
        result = -1

        for i in range(n):
            cities = self.bfs(i, adjList, distanceThreshold)
            if cities < minCities or (cities == minCities and i > result):
                minCities = cities
                result = i

        return result

            