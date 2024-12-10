""" 34. Find First and Last Position of Element in Sorted Array """

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        leftmost = findLeft(nums, target)
        rightmost = findRight(nums, target)

        # Check if the target exists in the array
        if leftmost <= rightmost and leftmost < len(nums) and nums[leftmost] == target:
            return [leftmost, rightmost]
        return [-1, -1]

