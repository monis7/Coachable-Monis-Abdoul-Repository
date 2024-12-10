""" 724. Find Pivot Index """

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            # Check if the current index is the pivot
            if 2 * left_sum + num == total_sum:
                return i
            # Update the left sum to include the current number
            left_sum += num
        return -1

