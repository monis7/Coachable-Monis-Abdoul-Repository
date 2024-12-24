""" 698. Partition to K Equal Sum Subsets """
from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, remainder = divmod(sum(nums), k)
        if remainder != 0 or max(nums) > target:
            return False

        nums.sort(reverse=True)
        used = [False] * len(nums)

        def backtrack(start, k, current_sum):
            if k == 0:
                return True
            if current_sum == target:
                return backtrack(0, k - 1, 0)
            for i in range(start, len(nums)):
                if not used[i] and current_sum + nums[i] <= target:
                    used[i] = True
                    if backtrack(i + 1, k, current_sum + nums[i]):
                        return True
                    used[i] = False
            return False

        return backtrack(0, k, 0)
