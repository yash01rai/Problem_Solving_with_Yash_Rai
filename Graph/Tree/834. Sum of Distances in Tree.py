# https://leetcode.com/problems/sum-of-distances-in-tree/?envType=daily-question&envId=2024-04-28
# https://www.youtube.com/results?search_query=Sum+of+distances

# Approach
# dfs1 to get depth of all the nodes from the root
# dfs2 to execute the formulae
# formulae: child node + its children would decrement 1 each node
# which mean decrement of child node + its children from the rootResult
# remaining nodes will again added to the rootResult
# updating the child


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]

        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        count = [0] * n
        resultRoot = 0

        def dfsRoot(node, prev, depth):
            nonlocal resultRoot

            total = 1
            resultRoot += depth

            for curr in adjList[node]:
                if curr == prev:
                    continue

                total += dfsRoot(curr, node, depth + 1)

            count[node] = total
            return total
        
        dfsRoot(0, -1, 0)

        print(count)

        result = [0] * n
        print(resultRoot)
        result[0] = resultRoot

        def dfsChildNodes(node, parent):

            for child in adjList[node]:
                if child == parent:
                    continue
                
                result[child] = result[node] - count[child] + (n - count[child])
                
                dfsChildNodes(child, node)

        dfsChildNodes(0, -1)
        return result