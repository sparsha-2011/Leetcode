# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Approach:
# This function removes duplicates from a sorted linked list by iterating through the list and skipping nodes with duplicate values.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        This function removes all duplicate elements from a sorted linked list.
        It iterates through the list, and whenever a duplicate value is found,
        it skips the duplicate node.

        Parameters:
        - head (ListNode): The head of the input sorted linked list.

        Returns:
        - ListNode: The head of the linked list after removing duplicates.
        """
        # If the list is empty, return None
        if not head:
            return None
        
        # Create a dummy node to simplify the head manipulation when removing duplicates
        dum = ListNode(0, head)

        # Initialize previous and current pointers
        prev = None
        cur = head
        prev = cur

        # Traverse the linked list
        while cur:
            # If current node's value is the same as the previous one, skip the current node
            if prev.val == cur.val:
                cur = cur.next
            else:
                # Otherwise, update previous node's next pointer and move both pointers forward
                prev.next = cur
                prev = cur
                cur = cur.next

        # Set the last node's next pointer to None to terminate the list
        prev.next = None

        # Return the list starting from the original head, which is now after the dummy node
        return dum.next
