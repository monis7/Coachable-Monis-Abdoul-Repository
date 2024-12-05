"""2875. Minimum Size Subarray in Infinite Array"""

from typing import List

class Solution:
	def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)  
        total_sum = sum(nums)  
        current_sum = 0 
        window_size = 0  
        min_length = float('inf')  
        full_cycle_contribution = (target // total_sum) * n
        target %= total_sum
        if target == 0:
            return full_cycle_contribution
        start = 0
        for end in range(2 * n):  
            current_sum += nums[end % n]
            window_size += 1
            while current_sum > target:
                current_sum -= nums[start % n]
                window_size -= 1
                start += 1
            if current_sum == target:
                min_length = min(min_length, window_size + full_cycle_contribution)
        return min_length if min_length != float('inf') else -1
