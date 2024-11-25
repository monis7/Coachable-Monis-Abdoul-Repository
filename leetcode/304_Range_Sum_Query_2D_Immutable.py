"""304. Range Sum Query 2D-Immutable"""

from collections import defaultdict
from typing import List

class Solution:
    """Solution Class"""
    def __init__(self, matrix: List[List[int]]):
       if not matrix or not matrix[0]:
           self.prefix = []
           return
       m, n = len(matrix), len(matrix[0])
       self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
       for i in range(1, m + 1):
           for j in range(1, n + 1):
               self.prefix[i][j] = matrix[i - 1][j - 1] \
                                 + self.prefix[i - 1][j] \
                                 + self.prefix[i][j - 1] \
                                 - self.prefix[i - 1][j - 1]
      
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
       row2, col2 = row2 + 1, col2 + 1
       row1, col1 = row1 + 1, col1 + 1
       total_sum = self.prefix[row2][col2]
       if row1 > 0:
           total_sum -= self.prefix[row1 - 1][col2]
       if col1 > 0:
           total_sum -= self.prefix[row2][col1 - 1]
       if row1 > 0 and col1 > 0:
           total_sum += self.prefix[row1 - 1][col1 - 1] 
       return total_sum
