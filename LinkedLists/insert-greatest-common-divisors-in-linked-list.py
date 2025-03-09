# Leetcode Problem: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        This function inserts the greatest common divisor (GCD) of consecutive nodes in a linked list 
        between the nodes in the list.
        """

        # Helper function to calculate GCD using Euclidean algorithm
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Initialize pointers to traverse the linked list
        cur = head.next
        prev = head

        # Traverse the linked list and insert the GCD between nodes
        while cur:
            # Create a new node for the GCD of prev and cur
            new_l = ListNode(gcd(prev.val, cur.val))
            
            # Insert the new node between prev and cur
            temp = prev.next
            prev.next = new_l
            new_l.next = temp
            
            # Move prev and cur to the next pair of nodes
            prev = cur
            cur = cur.next

        # Return the modified list
        return head
