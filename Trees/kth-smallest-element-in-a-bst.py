# LeetCode Problem: Kth Smallest Element in a BST
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Returns the kth smallest element in a binary search tree (BST).

        The function uses an in-order traversal of the tree, which ensures that
        the values are visited in ascending order. After the traversal, the k-1-th
        index in the result list will contain the kth smallest value.

        Time Complexity: O(n), where n is the number of nodes in the tree, as we visit each node once.
        Space Complexity: O(n), where n is the number of nodes, due to the recursion stack and result list.
        """

        res = []

        def inorder(node):
            if not node:
                return 

            inorder(node.left)  # Visit left subtree
            res.append(node.val)  # Append current node value
            inorder(node.right)  # Visit right subtree

        inorder(root)
        return res[k-1]  # Return the kth smallest element
