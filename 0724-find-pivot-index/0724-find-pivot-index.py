class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total = 0
        for num in nums :
            total += num
        
        left = 0

        for i in range (len(nums)) :
            right = total - left - nums[i]

            if left == right :
                return i
            
            left += nums[i]
        
        return -1
        