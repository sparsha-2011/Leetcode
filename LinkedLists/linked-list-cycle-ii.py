# LeetCode Link: https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Function to detect the start of the cycle in a linked list.
        
        This function uses Floyd's Tortoise and Hare algorithm to detect the cycle
        and then finds the entry point of the cycle.
        
        Time complexity: O(n), where n is the number of nodes in the linked list.
        Space complexity: O(1), since we only use two pointers.
        """
        
        slow, fast = head, head
        
        # Step 1: Detect if there is a cycle using two pointers (slow and fast)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Cycle detected
                break
        else:
            # No cycle found
            return None

        # Step 2: Find the entry point of the cycle
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next

        return slow  # The node where slow and fast meet is 
