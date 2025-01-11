""" 114. Flatten Binary Tree to Linked List """
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            if not node:
                return None
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            return right_tail or left_tail or node
        dfs(root)
