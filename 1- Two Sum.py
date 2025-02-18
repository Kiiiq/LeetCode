class Solution(object):
    def twoSum(self, nums, target):
        needed= dict()
    
        for i in range(0,len(nums)):
            if nums[i] in needed:
                return [i,needed[nums[i]]]
            needed.update({target-nums[i]:i})
        