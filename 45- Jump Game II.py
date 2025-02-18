class Solution:
    def jump(self, nums: List[int]) -> int:
        nums[len(nums)-1]=9999
        jumps= 0
        place= 0
        temp=0
    
        while(True):
            if nums[place]==9999:
                return jumps

            for x in range(0,nums[place]+1):
                try:
                    if nums[place+x]+x>=temp:
                        temp=nums[place+x]+x
                        positionToGo=x

                    if positionToGo==0:
                        positionToGo=nums[place]
                
                except:
                    return jumps+1
            
            place=place+positionToGo
            jumps=jumps+1
            temp=0