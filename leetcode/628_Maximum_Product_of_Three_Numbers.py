""" 628. Maximum Product of Three Numbers """

from typing import List
import math

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Initialize variables to find top 3 and bottom 2 numbers
        max1, max2, max3 = -math.inf, -math.inf, -math.inf
        min1, min2 = math.inf, math.inf

        for num in nums:
            # Update top 3 maximums
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num

            # Update bottom 2 minimums
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)

