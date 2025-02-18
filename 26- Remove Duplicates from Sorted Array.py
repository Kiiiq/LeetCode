class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueNumbers = 0
        temp= int

        for num in range(0, len(nums)):
            if temp != nums[num]:
                temp=nums[num]
                nums[uniqueNumbers]=nums[num]
                uniqueNumbers=uniqueNumbers+1


        return uniqueNumbers