""" 1372. Longest ZigZag Path in a Binary Tree """
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, direction, length):
            if not node:
                return length - 1
            if direction == 'left':
                return max(dfs(node.left, 'right', length + 1), dfs(node.right, 'left', 1))
            else:
                return max(dfs(node.right, 'left', length + 1), dfs(node.left, 'right', 1))

        return dfs(root, 'left', 0)
