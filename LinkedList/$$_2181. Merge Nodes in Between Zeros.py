# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/?envType=daily-question&envId=2024-07-04
# $$ -> Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 𝐔𝐧𝐝𝐞𝐫𝐬𝐭𝐚𝐧𝐝𝐢𝐧𝐠
        # Given a Linked List, we need to return a modified list where nodes between two consecutive zero values should be merged together into a single node

        # 𝐀𝐩𝐩𝐫𝐨𝐚𝐜𝐡
        # We will use two pointers, 𝐭𝐦𝐩 and 𝐜𝐮𝐫𝐫
        # curr will traverse through the list, collecting values between two consecutive zero nodes
        # tmp will always point to the node next to the current zero value node.
        # When the curr node reaches the next zero value node:
        # we will update the value of the tmp node to the sum of the collected values by the curr node
        # Reset the sum to zero
        # Point the tmp node to the node next to the current zero value node
        # Finally, move the curr node forward and assign curr node to tmp

        # 𝐂𝐨𝐦𝐩𝐥𝐞𝐱𝐢𝐭𝐢𝐞𝐬
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        curr = head.next
        tmp = curr
        node_sum = 0

        while curr:
            
            while curr.val != 0:
                node_sum += curr.val
                curr = curr.next

            tmp.val = node_sum
            node_sum = 0
            tmp.next = curr.next
            curr = curr.next
            tmp = curr

        return head.next