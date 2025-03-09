# Problem Link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Approach: 
# We use a divide and conquer approach, where we find the middle element of the linked list 
# and make it the root of the BST. Then, we recursively repeat this process for the left and 
# right sublists to construct the left and right subtrees.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMiddle(self, head: ListNode) -> ListNode:
        """
        This helper function finds the middle element of the linked list using 
        the slow and fast pointer approach.
        """
        slow, fast = head, head
        prev = None

        # Traverse the list with slow and fast pointers to find the middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Disconnect the left half of the list to avoid circular references
        if prev:
            prev.next = None

        return slow

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        This function converts a sorted linked list to a height balanced binary search tree.
        It recursively finds the middle node, makes it the root of the BST, and repeats the
        process for the left and right sublists.
        """
        if not head:
            return None

        # Find the middle element of the list
        mid = self.findMiddle(head)

        # Create a tree node with the middle value
        root = TreeNode(mid.val)

        # Recursively build the left and right subtrees
        if head != mid:
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(mid.next)

        return root
