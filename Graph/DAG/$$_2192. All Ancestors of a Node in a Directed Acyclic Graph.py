class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        
        adjList = defaultdict(list)
        #  S.C. O(V + E)

        for u, v in edges:
            adjList[u].append(v)

        result = [[] for i in range(n)]

        def dfs(node, parent):

            for adjNode in adjList[node]:
                if not result[adjNode] or result[adjNode][-1] != parent:
                    result[adjNode].append(parent)
                    dfs(adjNode, parent)
            
        
        for i in range(n):
            dfs(i, i)
        
        # T.C. O(V * (V + E))
        return result


        # topological sort approach


        # revesing the direction approach
