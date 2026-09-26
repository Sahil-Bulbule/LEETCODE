class Solution:
    def evaluate(self, s, knowledge):
        mp = {}

        for key, value in knowledge:
            mp[key] = value

        result = ""
        i = 0

        while i < len(s):

            if s[i] == "(":
                j = i + 1

                while s[j] != ")":
                    j += 1

                key = s[i + 1:j]

                result += mp.get(key, "?")

                i = j + 1

            else:
                result += s[i]
                i += 1

        return result