""" 408. Valid Word Abbreviation """
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
            elif word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                return False
        return i == len(word) and j == len(abbr)
