""" 113. Path Sum II """
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path, remaining):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and remaining == node.val:
                result.append(list(path))
            else:
                dfs(node.left, path, remaining - node.val)
                dfs(node.right, path, remaining - node.val)
            path.pop()
        result = []
        dfs(root, [], targetSum)
        return result
