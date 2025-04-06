# LeetCode Problem: Construct Binary Tree from Preorder and Inorder Traversal
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Reconstructs a binary tree from its preorder and inorder traversal lists.

        The first element in preorder is always the root. In inorder, elements to the
        left of the root are in the left subtree, and elements to the right are in the right subtree.

        Time Complexity: O(n^2) in the worst case due to slicing and index searches.
        Space Complexity: O(n^2) for recursive stack and array slices.
        """

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
