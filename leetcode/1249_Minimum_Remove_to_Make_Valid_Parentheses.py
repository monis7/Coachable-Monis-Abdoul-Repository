""" 1249. Minimum Remove to Make Valid Parentheses """
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalid_indices = set()
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    invalid_indices.add(i)
        
        while stack:
            invalid_indices.add(stack.pop())
        
        return ''.join([char for i, char in enumerate(s) if i not in invalid_indices])

