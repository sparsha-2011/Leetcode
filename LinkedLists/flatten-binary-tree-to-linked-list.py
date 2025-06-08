# Leetcode Problem: Flatten Binary Tree to Linked List
# Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Author: Sparsha Srinath
# Date: 2025-06-08
# Tags: Binary Tree, DFS, Recursion, Iteration, Morris Traversal
# Problem Statement:
#    Given the root of a binary tree, flatten the tree into a "linked list":
#    - The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list
#    - The left child pointer should always be None
#    - The "linked list" should be in the same order as a preorder traversal of the binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Approach 1: Recursive DFS
# Time Complexity: O(n)
# Space Complexity: O(n) for recursion stack
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            if not node.left and not node.right:
                return node
            
            leftTail = dfs(node.left)
            rightTail = dfs(node.right)

            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None

            return rightTail or leftTail

        dfs(root)


# Approach 2: Iterative using Stack
# Time Complexity: O(n)
# Space Complexity: O(n) for the explicit stack
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        stack = [root]
        prev = None

        while stack:
            curr = stack.pop()
            if prev:
                prev.right = curr
                prev.left = None

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            prev = curr


# Approach 3: Morris Traversal (Threaded Binary Tree)
# Time Complexity: O(n)
# Space Complexity: O(1) – no recursion or explicit stack
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root

        while curr:
            if curr.left:
                # Find the rightmost node in the left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                # Threading: connect rightmost node to current's right subtree
                prev.right = curr.right
                # Move left subtree to right
                curr.right = curr.left
                curr.left = None
            # Move to next right node
            curr = curr.right
