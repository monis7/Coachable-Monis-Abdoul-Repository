""" 713. Subarray Product Less Than K """

from typing import List

class Solution:
	def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        product = 1
        count = 0
        left = 0
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left <= right:
                product /= nums[left]
                left += 1
            count += right - left + 1
        return count
