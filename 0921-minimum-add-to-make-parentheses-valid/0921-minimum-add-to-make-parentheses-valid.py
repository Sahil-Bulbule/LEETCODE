class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = added = 0
        for ch in s:
            if ch == "(":
                opened += 1
            elif opened:  # close a pending "("
                opened -= 1
            else:  # ")" with nothing to close -> add a "("
                added += 1
        return added + opened  # still-open "(" need a ")" each