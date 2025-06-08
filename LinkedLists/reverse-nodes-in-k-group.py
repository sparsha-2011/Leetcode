# Author: Sparsha Srinath
# Date: 2025-06-08
# URL: https://leetcode.com/problems/reverse-nodes-in-k-group/
# Tags: Linked List, Two Pointers, In-place Reversal, Group Reversal
# Description: Reverses nodes in k-group chunks in a linked list.

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.get_kth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp

        return dummy.next

    def get_kth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
