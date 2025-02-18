class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        uniqueNumbers=0

        for num in range(0, len(nums)):
            if val != nums[num]:
                nums[uniqueNumbers]=nums[num]
                uniqueNumbers= uniqueNumbers+1
        
        return uniqueNumbers