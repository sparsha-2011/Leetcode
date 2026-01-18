# Author: Sparsha Srinath
# Date: 2025-08-13
# Problem: Remove Nth Node From End of List
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Tags: Linked List, Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return None

        cur = head
        dummy = ListNode(0, cur)
        
        total = 0
        while cur:
            total += 1
            cur = cur.next
            
        if n == total:
            return head.next

        cur = head
        prev = head
        for i in range(total - n):
            prev = cur
            cur = cur.next

        print(prev, cur)
        prev.next = cur.next

        return dummy.next
