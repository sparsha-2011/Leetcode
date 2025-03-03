# LeetCode Problem: https://leetcode.com/problems/odd-even-linked-list/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Rearranges a linked list such that all nodes at odd indices appear before all nodes at even indices.
        Maintains the relative order of both odd and even indexed nodes.
        
        Time Complexity: O(n) - Traverses the list once.
        Space Complexity: O(1) - Modifies the list in place.
        
        :param head: Head of the singly linked list
        :return: Modified head of the linked list
        """
        if head == None or head.next == None:
            return head

        odd = head
        even = head.next
        evenStart = even  # Keep track of the start of even nodes

        # Iterate while there are nodes to process
        while odd != None and even != None and odd.next != None and even.next != None:
            odd.next = even.next  # Link current odd node to the next odd node
            odd = odd.next  # Move odd pointer forward
            even.next = odd.next  # Link current even node to the next even node
            even = even.next  # Move even pointer forward
        
        odd.next = evenStart  # Append even list after odd list
        return head
