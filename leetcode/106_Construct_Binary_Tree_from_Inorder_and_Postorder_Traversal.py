""" 106. Construct Binary Tree from Inorder and Postorder Traversal """
from typing import Optional, List

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

            root_val = postorder.pop()
            root = TreeNode(root_val)
            idx = idx_map[root_val]

            root.right = helper(idx + 1, in_right)
            root.left = helper(in_left, idx - 1)
            
            return root

        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
