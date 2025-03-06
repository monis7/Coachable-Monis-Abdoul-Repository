""" 230. Kth Smallest Element in a BST """
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            nonlocal k, result
            if not node or result is not None:
                return
            inorder(node.left)
            k -= 1
            if k == 0:
                result = node.val
                return
            inorder(node.right)
        result = None
        inorder(root)
        return result
