""" 1762. Buildings with an Ocean View """
from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res, max_height = [], 0
        for i in reversed(range(len(heights))):
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]
        return res[::-1]
