""" 39. Combination Sum """
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remain, combo, start):
            if remain == 0:
                result.append(list(combo))
                return
            elif remain < 0:
                return
            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                backtrack(remain - candidates[i], combo, i)
                combo.pop()

        result = []
        backtrack(target, [], 0)
        return result
