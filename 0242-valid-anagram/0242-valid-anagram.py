class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # s = "anagram"
        # t = "nagaram"

        dict = {}
        for x in s :
            if x in dict :
                dict[x] += 1
            else :
                dict[x] = 1

        for x in t :
            if x in dict :
               dict[x] -= 1
            else :
                return False
        
        for x in dict :
            if dict[x] != 0 :
                return False
        return True
        