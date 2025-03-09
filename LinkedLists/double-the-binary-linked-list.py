# Problem link: https://leetcode.com/problems/double-the-binary-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Reverse the linked list to make operations easier
        cur = head
        prev = None
         
        while cur:
            next_n = cur.next
            cur.next = prev
            prev = cur
            cur = next_n

        new_start = prev  # new_start is now the head of the reversed linked list
        carry = 0
        sum_l = 0
        digit = 0

        # Step 2: Traverse the reversed list and double each value
        while prev:
            sum_l = prev.val * 2 + carry
            digit = sum_l % 10
            prev.val = digit
            carry = sum_l // 10  # Carry for the next node
            prev = prev.next

        # Step 3: If there's a carry left, create a new node
        if carry != 0:
            new_l = ListNode(carry)
            last_node = new_start
            # Traverse to the end of the list and append the carry node
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_l

        # Step 4: Reverse the list back to restore the original order
        prev_last = None
        while new_start:
            next_n = new_start.next
            new_start.next = prev_last
            prev_last = new_start
            new_start = next_n

        return prev_last  # Return the head of the final modified linked list
