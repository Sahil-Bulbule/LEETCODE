class Solution(object):
    def twoSum(self, nums, target):

        mp = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in mp:
                return [mp[need],i]
            mp[nums[i]] = i