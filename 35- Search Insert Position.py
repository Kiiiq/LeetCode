class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        min= 0
        max= len(nums)-1
        
        while max>min:
            if target>nums[((min+max)//2)]:
                min=(min+max)//2+1
            elif target<nums[((min+max)//2)]:
                max=(min+max)//2-1
            else:
                return (((min+max)//2))
        
        if target>nums[((min+max)//2)]:
            return ((min+max)//2)+1
        else:
            return ((min+max)//2)