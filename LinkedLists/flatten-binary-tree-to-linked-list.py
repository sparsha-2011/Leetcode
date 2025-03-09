# LeetCode Problem: Flatten Binary Tree to Linked List
# Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flatten a binary tree to a linked list in-place using preorder traversal.
        
        The tree is modified such that the left child of every node is None 
        and the right child points to the next node in the preorder traversal.
        
        :param root: The root node of the binary tree.
        :return: None (The tree is modified in place).
        
        Time Complexity: O(n) where n is the number of nodes in the tree.
        Space Complexity: O(n) for the stack used in the iterative traversal.
        """
        # Edge case: If the root is None, there's nothing to flatten
        if not root:
            return []

        # Initialize the current node pointer and the stack to hold nodes
        cur = root
        stack = [root]

        # Iterate while there are nodes left to process
        while stack:
            node = stack.pop()  # Pop the current node from the stack

            # Skip the first iteration since root doesn't need modification
            if node != root:
                cur.right = node  # Attach the node to the current node's right
                cur.left = None   # Set the left child to None (flatten the tree)

            cur = node  # Move the current pointer to the node

            # Push right and left children to the stack (if they exist) for processing
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        # Return the modified root (it's flattened in place)
        return root
