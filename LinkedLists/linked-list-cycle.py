# Author: Sparsha Srinath
# Date: 2025-11-09
# Problem: Linked List Cycle Detection
# Link: https://leetcode.com/problems/linked-list-cycle/
# Tags: Linked List, Two Pointers, Floyd's Cycle Detection
# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
