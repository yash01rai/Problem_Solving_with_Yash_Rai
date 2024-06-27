# https://leetcode.com/problems/find-center-of-star-graph/?envType=daily-question&envId=2024-06-27
# $ - Easy, $$ - Medium, $$$ - Hard

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        # star graph property -> center node will have more than 1 adjacent node
        
        adjList = defaultdict(list)

        for u, v in edges:
            if u in adjList:
                return u

            if v in adjList:
                return v

            adjList[u].append(v)
            adjList[v].append(u)

    