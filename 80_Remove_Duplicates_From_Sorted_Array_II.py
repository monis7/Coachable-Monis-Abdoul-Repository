"""80. Remove Duplicates From Sorted Array II"""

from collections import defaultdict
from typing import List

class Solution:
    """Solution Class"""
    def removeDuplicates(self, nums: List[int]) -> int:
       i = 2 
       for j in range(2, len(nums)):
           if nums[j] != nums[i - 2]:
               nums[i] = nums[j]
               i += 1
       return i
