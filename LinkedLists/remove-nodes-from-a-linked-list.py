# Author: Sparsha Srinath
# Date: 2025-08-13
# Problem: Remove Nodes From Linked List
# Link: https://leetcode.com/problems/remove-nodes-from-linked-list/
# Tags: Linked List, Stack, Monotonic Stack
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding recursion / helper reversal)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(cur):
            prev = None
            while cur:
                next_n = cur.next
                cur.next = prev
                prev = cur
                cur = next_n
            return prev
        
        rev_head = reverse(head)
        cur = rev_head
        prev = None

        while cur:
            if prev and prev.val > cur.val:
                prev.next = cur.next
                cur = prev.next
                continue

            prev = cur
            cur = cur.next
        
        return reverse(rev_head)
