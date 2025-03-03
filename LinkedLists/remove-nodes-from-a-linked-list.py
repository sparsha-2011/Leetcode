# LeetCode: https://leetcode.com/problems/remove-nodes-from-linked-list/
# Problem: Given the head of a linked list, remove every node that has a node 
# with a greater value anywhere to the right.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        """
        Reverse the list, remove nodes with smaller values, then reverse back.

        Time Complexity: O(n) - We traverse the list 3 times (reverse, process, reverse back)
        Space Complexity: O(1) - In-place modification
        """
        
        # Step 1: Reverse the linked list
        prev, cur = None, head
        while cur:
            next_n = cur.next
            cur.next = prev
            prev = cur
            cur = next_n
        head = prev  # New head after reversal

        # Step 2: Remove nodes with a greater value on the left (original right)
        max_val = head.val
        cur = head
        while cur and cur.next:
            if cur.next.val < max_val:
                cur.next = cur.next.next  # Remove node
            else:
                cur = cur.next
                max_val = cur.val  # Update max value

        # Step 3: Reverse the list back to restore original order
        prev, cur = None, head
        while cur:
            next_n = cur.next
            cur.next = prev
            prev = cur
            cur = next_n

        return prev  # New head after final reversal
