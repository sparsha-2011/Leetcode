## LeetCode Problem: Merge Two Sorted Lists
# Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists and returns the head of the merged list.
        :param list1: Head of the first sorted linked list
        :param list2: Head of the second sorted linked list
        :return: Head of the merged sorted linked list
        """
        
        # Create a dummy node to act as the starting point of the merged list
        dummy = ListNode()
        cur = dummy
        
        # Traverse both lists and merge them in sorted order
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        # If one of the lists is not fully traversed, append the remaining elements
        cur.next = list1 if list1 else list2
        
        return dummy.next
