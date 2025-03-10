# LeetCode Problem Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        cur = head
        slow, fast = head, head
        max_sum = 0

        # Step 1: Use fast and slow pointers to find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            node_n = slow.next
            slow.next = prev
            prev = slow
            slow = node_n
        
        # Step 3: Compare twin pairs (first half and reversed second half)
        first = head
        second = prev
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum
