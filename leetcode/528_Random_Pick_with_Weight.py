""" 528. Random Pick with Weight """
import random

class Solution:
    def __init__(self, w):
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)
        self.total_sum = total

    def pickIndex(self) -> int:
        target = random.uniform(0, self.total_sum)
        left, right = 0, len(self.prefix_sums) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix_sums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left
