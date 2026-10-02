class Solution:
    def generateParenthesis(self, n):
        ans = []

        def backtrack(s, open, close):
            # A complete valid combination is formed
            if len(s) == 2 * n:
                ans.append(s)
                return

            # Add '(' if we still have opening brackets available
            if open < n:
                backtrack(s + "(", open + 1, close)

            # Add ')' only when it is safe
            if close < open:
                backtrack(s + ")", open, close + 1)

        backtrack("", 0, 0)

        return ans