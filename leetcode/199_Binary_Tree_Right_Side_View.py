""" 199. Binary Tree Right Side View """
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result, queue = [], deque([root])
        while queue:
            rightmost = None
            for _ in range(len(queue)):
                node = queue.popleft()
                rightmost = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(rightmost.val)
        return result
