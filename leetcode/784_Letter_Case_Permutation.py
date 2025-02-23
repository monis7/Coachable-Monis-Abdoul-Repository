""" 784. Letter Case Permutation """
from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(index, path):
            if index == len(s):
                result.append("".join(path))
                return
            if s[index].isalpha():
                backtrack(index + 1, path + [s[index].lower()])
                backtrack(index + 1, path + [s[index].upper()])
            else:
                backtrack(index + 1, path + [s[index]])

        result = []
        backtrack(0, [])
        return result
