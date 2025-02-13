""" 1570. Dot Product of Two Sparse Vectors """
from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.mapping = {i: num for i, num in enumerate(nums) if num != 0}

    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum(self.mapping[i] * vec.mapping[i] for i in self.mapping if i in vec.mapping)
