# Author: Sparsha Srinath
# Date: 2025-08-13
# Problem: Double a Number Represented as a Linked List
# Link: https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
# Tags: Linked List, Math
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(cur):
            prev = None
            while cur:
                next_n = cur.next
                cur.next = prev
                prev = cur
                cur = next_n
            
            return prev
        
        l1 = reverse(head)
        carry = 0
        dummy = ListNode()
        add = dummy

        while l1 or carry:
            num = l1.val if l1 else 0
            total = (2 * num) + carry
            d = total % 10
            carry = total // 10

            add.next = ListNode(d)
            add = add.next

            l1 = l1.next if l1 else None
        
        res = reverse(dummy.next)
        return res
