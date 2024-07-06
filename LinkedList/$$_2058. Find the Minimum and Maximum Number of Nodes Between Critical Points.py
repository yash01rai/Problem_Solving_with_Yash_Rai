# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        # what is crtical nodes and what is not?
        # how to identify the nodes
        # prev > curr < next or prev < curr > next
        # what is min distance
        # what is max distance

        # Understanding
        # We have to find the minimum and maximum distance between two critical nodes
        # Critical node will have value prev > curr < next or prev < curr > next 

        # Observations
        # If you observe then you notice that first critical node and last critical node will have the maximum distance
        # And two consecutive critical nodes will have a chance of having the minimum distance

        # Approach
        # Treverse through the Linked List
        # Maintain a nodeNumber to identify where you are in the Linked List and also store previous node in a variable
        # Look for firstCriticalNode and lastCriticalNode to get the maximum distance
        # And also check prevCriticalNode and current critical node for minimum distance
        # retrun the result if found, if not return [-1, -1]


        minDistance = inf
        maxDistance = -1

        firstCriticalNode = 0
        lastCriticalNode = 0

        prevCriticalNode = 0

        prevNode = None
        curr = head
        nodeNumber = 1

        while curr:

            if prevNode and curr.next and (prevNode.val > curr.val < curr.next.val or prevNode.val < curr.val > curr.next.val):
                if firstCriticalNode == 0:
                    firstCriticalNode = nodeNumber
                
                if firstCriticalNode != nodeNumber:
                    lastCriticalNode = nodeNumber

                if prevCriticalNode != 0 and prevCriticalNode != nodeNumber:
                    minDistance = min(nodeNumber - prevCriticalNode, minDistance)

                prevCriticalNode = nodeNumber
            
            prevNode = curr
            curr = curr.next
            nodeNumber += 1

        if firstCriticalNode != 0 and lastCriticalNode != 0:
            maxDistance = lastCriticalNode - firstCriticalNode
        
        if minDistance == inf:
            minDistance = -1

        return [minDistance, maxDistance]



        
