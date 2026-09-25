class Solution(object):
    def braceExpansionII(self, expression):
        
        result = set()

        def solve(s):
            # Agar braces nahi bache
            if '{' not in s:
                result.add(s)
                return

            # Pehla closing brace
            j = s.find('}')

            # Uske corresponding opening brace
            i = s.rfind('{', 0, j)

            # Brace ke andar ke options
            options = s[i + 1:j].split(',')

            # Har option ko replace karke recursion
            for option in options:
                new_s = s[:i] + option + s[j + 1:]
                solve(new_s)

        solve(expression)

        return sorted(result)