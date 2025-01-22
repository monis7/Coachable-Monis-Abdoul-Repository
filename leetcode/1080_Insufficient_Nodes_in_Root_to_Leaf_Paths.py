""" 1080. Insufficient Nodes in Root to Leaf Paths """
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node, sum_):
            if not node:
                return None
            sum_ += node.val
            if not node.left and not node.right:
                return node if sum_ >= limit else None
            node.left = dfs(node.left, sum_)
            node.right = dfs(node.right, sum_)
            return node if node.left or node.right else None

        return dfs(root, 0)
