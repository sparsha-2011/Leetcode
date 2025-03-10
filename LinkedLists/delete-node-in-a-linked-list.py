# LeetCode Problem Link: https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        Deletes a node from a singly-linked list, given only access to that node.
        
        Note: This method does not return anything; it modifies the linked list in-place.

        Args:
        node (ListNode): The node to be deleted (except the tail).

        Returns:
        None
        """
        if node and node.next:
            node.val = node.next.val  # Copy the value of the next node to the current node
            node.next = node.next.next  # Delete the next node by skipping it
