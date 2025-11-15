# Author: Sparsha Srinath
# Date: 2025-06-08
# URL: https://leetcode.com/problems/reorder-list/
# Tags: Linked List, Two Pointers, In-place Reversal, Merge

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders a linked list so that it follows the pattern:
        L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

        Modifies the list in-place and returns None.

        Args:
            head (Optional[ListNode]): The head of the linked list.
        """

        if not head or not head.next:
            return

        # Step 1: Find middle of the linked list using slow and fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        second_half = slow.next
        slow.next = None
        prev = None
        while second_half:
            next_node = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = next_node

        # Step 3: Merge the first half and the reversed second half
        first = head
        second = prev
        while second:
            f_next = first.next
            s_next = second.next

            first.next = second
            second.next = f_next

            first = f_next
            second = s_next


#Solution 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dum = ListNode()
        slow = head
        fast = head
        prev = None

        while fast.next and fast.next.next :
            slow = slow.next
            fast= fast.next.next

        second_half = slow.next
        slow.next = None
        
        while second_half:
            next_node = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = next_node
        
        first = head
        second = prev

        i = 0
        while first:
            if i%2==0:
                dum.next = first
                first=first.next
            else:
                dum.next = second
                second=second.next
            i+=1
            dum = dum.next

      
        if second:
            dum.next = second





      
