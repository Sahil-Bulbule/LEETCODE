class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        ans = n

        for i in range(n) :
            ans ^= i
            ans ^= nums[i]

        return ans
        