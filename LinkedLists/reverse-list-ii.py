# Author: Sparsha Srinath  
# Date: 2025-11-09  
# Problem: Reverse Linked List II  
# Link: https://leetcode.com/problems/reverse-linked-list-ii/  
# Tags: Linked List, Reversal, Pointers  
# Time Complexity: O(N)   # Single traversal through the list  
# Space Complexity: O(1)  # Constant extra space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        # Dummy node simplifies handling edge cases (like reversing from the head)
        dum = ListNode(0, head)
        prev = None
        leftprev = dum
        cur = head
         
        # Step 1: Move pointers to the start of the sublist (left)
        for _ in range(left - 1):
            leftprev = cur
            cur = cur.next 
        
        # Step 2: Reverse the sublist from left to right
        for _ in range(right - left + 1):
            next_n = cur.next
            cur.next = prev
            prev = cur
            cur = next_n
        
        # Step 3: Reconnect reversed portion with the rest of the list
        leftprev.next.next = cur
        leftprev.next = prev

        # Step 4: Return the updated head
        return dum.next
