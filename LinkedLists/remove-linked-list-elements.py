# LeetCode Problem Link: https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Removes all elements from a linked list that have the given value.

        Args:
        head (Optional[ListNode]): The head of the linked list.
        val (int): The value to remove from the linked list.

        Returns:
        Optional[ListNode]: The head of the modified linked list.
        """
        
        # Create a dummy node that points to the head
        dummy = ListNode(0, head)
        current = dummy

        # Traverse the list and remove nodes with the given value
        while current:
            while current.next and current.next.val == val:
                current.next = current.next.next  # Skip the node with the target value
            current = current.next
        
        return dummy.next  # Return the modified list without the dummy node
