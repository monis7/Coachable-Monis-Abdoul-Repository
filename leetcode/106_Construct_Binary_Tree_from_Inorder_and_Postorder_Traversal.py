""" 106. Construct Binary Tree from Inorder and Postorder Traversal """
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            if in_left > in_right:
                return None

            # The current root value is the last element in postorder
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # Index of the root in the inorder traversal
            idx = idx_map[root_val]

            # Recursively build the right and left subtrees
            root.right = helper(idx + 1, in_right)
            root.left = helper(in_left, idx - 1)

            return root

        # Build a hashmap to store the index of each value in inorder traversal
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        return helper(0, len(inorder) - 1)
