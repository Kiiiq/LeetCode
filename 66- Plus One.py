class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]+=1
    
        try:
            for i in range(1,len(digits)+1):
                if digits[-i]>=10:
                    digits[-i-1]+=1
                    digits[-i]=0
        except:
            digits.insert(0,0)
            for i in range(1,len(digits)+1):
                if digits[-i]>=10:
                    digits[-i-1]+=1
                    digits[-i]=0
                    
        return digits