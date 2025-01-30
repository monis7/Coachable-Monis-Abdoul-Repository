""" 429. N-ary Tree Level Order Traversal """
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return []
        result, queue = [], [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                queue.extend(node.children)
            result.append(level)
        return result
