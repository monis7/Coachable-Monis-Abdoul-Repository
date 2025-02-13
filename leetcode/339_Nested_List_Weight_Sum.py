""" 339. Nested List Weight Sum """
from typing import List

class NestedInteger:
    def __init__(self, value=None):
        self.value = value
        self.is_integer = isinstance(value, int)
        self.list = [] if not self.is_integer else None

    def isInteger(self) -> bool:
        return self.is_integer

    def getInteger(self) -> int:
        return self.value if self.is_integer else None

    def getList(self) -> List['NestedInteger']:
        return self.list if not self.is_integer else None

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(lst, depth):
            total = 0
            for ni in lst:
                if ni.isInteger():
                    total += ni.getInteger() * depth
                else:
                    total += dfs(ni.getList(), depth + 1)
            return total
        
        return dfs(nestedList, 1)
