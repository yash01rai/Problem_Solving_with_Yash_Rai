from collections import defaultdict

class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:

        # Idea behind the approach
        # Storing each co-ordinate max(furthest) absolute direction in a dictionary
        # which implies the opposite of the same cordinate should not be same character

        # After storing we sort the dictionary in increasing co-ordinates
        # which implies we are checking points traversing from inside (0,0) to outside
        # trying to reach the furthest square which can be achieved

        ptstag = defaultdict(set)    
        top = float('inf')
        
        # storing char using max abs co-ordinate
        for (x, y), tag in zip(points, s):
            r = max(abs(x), abs(y))

            if tag in ptstag[r] and r < top:
                top = r

            ptstag[r].add(tag)

        visited = []
        maxi = 0
        
        # counting the max number points which can form a square
        for r in sorted(ptstag):
            if r >= top:
                return maxi

            tmp = 0
            for v in ptstag[r]:
                if v in visited:
                    return maxi
                else:
                    tmp += 1
                    visited.append(v)
            maxi += tmp

        return maxi