""" 1372. Longest ZigZag Path in a Binary Tree """
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
        def longestZigZag(self, root: Optional[TreeNode]) -> int:
            def dfs(node, is_left: bool, length: int) -> int:
                if not node:
                    return length - 1
                if is_left:
                    return max(dfs(node.left, False, length + 1), dfs(node.right, True, 1))
                else:
                    return max(dfs(node.right, True, length + 1), dfs(node.left, False, 1))
            return dfs(root, True, 0)
