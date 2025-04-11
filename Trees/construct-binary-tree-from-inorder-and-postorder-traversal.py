#LeetCode Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        Reconstructs a binary tree from its inorder and postorder traversal lists.

        Args:
            inorder (List[int]): The inorder traversal of the binary tree.
            postorder (List[int]): The postorder traversal of the binary tree.

        Returns:
            TreeNode: The root of the reconstructed binary tree.

        
        """
        # Base case: if inorder is empty, there's no tree to build
        if not inorder:
            return None
        
        # The last element in postorder is always the root of the current subtree
        root_val = postorder.pop()
        root = TreeNode(root_val)

        # Find the index of the root in inorder to divide left and right subtrees
        index = inorder.index(root_val)

        # Important: build right subtree first because we're consuming postorder from the end
        root.right = self.buildTree(inorder[index + 1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)

        return root
