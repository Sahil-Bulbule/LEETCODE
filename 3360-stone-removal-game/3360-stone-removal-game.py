class Solution:
    def canAliceWin(self, n: int) -> bool:
        return ((isqrt(433 - 8 * n) - 1) & 2) == 0