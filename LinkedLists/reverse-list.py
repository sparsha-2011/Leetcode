# LeetCode Problem: https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list.

        :param head: The head of the linked list.
        :return: The new head of the reversed linked list.
        """
        cur = head
        prev = None

        # Traverse the list and reverse the links
        while cur:
            next_n = cur.next  # Store next node
            cur.next = prev  # Reverse the link
            prev = cur  # Move prev to current
            cur = next_n  # Move current to next node

        return prev  # New head of the reversed list
