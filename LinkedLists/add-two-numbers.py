# Author: Sparsha Srinath
# Date: 2025-08-13
# Problem: Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/
# Tags: Linked List, Math, Recursion
# Time Complexity: O(max(m, n))
# Space Complexity: O(max(m, n)) for the result list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
       

        carry = 0
        dummy = ListNode()
        add = dummy

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            d = total % 10

            add.next = ListNode(d)
            add = add.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
