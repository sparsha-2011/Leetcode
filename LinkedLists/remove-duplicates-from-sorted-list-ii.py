# LeetCode Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a sorted linked list, delete all duplicates such that each element 
        appears only once and return the linked list's head.
        """
        hash_map = {}  # Initialize a dictionary to store frequency of each value
        dum = ListNode(0, head)  # Create a dummy node to simplify edge cases (e.g., empty list, single node)
        cur = head
        
        # Traverse the list and count the frequency of each node's value
        while cur:
            hash_map[cur.val] = hash_map.get(cur.val, 0) + 1
            cur = cur.next
        
        # Print the frequency map for debugging purposes
        print(hash_map)
        
        prev = dum  # Initialize the previous node to dummy (start of the list)
        cur = head   # Start from the head of the list
        
        # Iterate over the linked list
        while cur:
            if hash_map[cur.val] == 1:  # If the current value appears only once
                prev.next = cur  # Keep the current node in the list
                prev = cur  # Move the prev pointer forward
            else:  # If the current value appears more than once
                prev.next = cur.next  # Skip the current node
            cur = cur.next  # Move the current pointer forward
        
        prev.next = None  # Ensure the last node's next pointer is None
        
        # Return the modified list, skipping the dummy node
        return dum.next
