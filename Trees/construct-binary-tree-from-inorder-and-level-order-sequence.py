from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], levelorder: List[int]) -> TreeNode:
        """
        Constructs a binary tree from inorder and level order traversal sequences.

        Args:
            inorder (List[int]): Inorder traversal of the tree.
            levelorder (List[int]): Level order traversal of the tree.

        Returns:
            TreeNode: Root of the constructed binary tree.
        """

        if not inorder or not levelorder:
            return None

        # The first element of level order is the root
        root_val = levelorder.pop(0)
        root = TreeNode(root_val)

        # Find index of root in inorder to split left and right
        root_index = inorder.index(root_val)
        left_inorder = set(inorder[:root_index])
        right_inorder = set(inorder[root_index + 1:])

        # Filter levelorder to get nodes for left and right subtrees
        left_level = [x for x in levelorder if x in left_inorder]
        right_level = [x for x in levelorder if x in right_inorder]

        # Recursive calls
        root.left = self.buildTree(inorder[:root_index], left_level)
        root.right = self.buildTree(inorder[root_index + 1:], right_level)

        return root
