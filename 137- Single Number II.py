class Solution(object):
    def singleNumber(self, nums):
        numeros= dict()
        lista=[]

        for nums in nums:
            try:
                numeros.update({nums:numeros.get(nums)+1})
            except:
                numeros.update({nums:1})
                lista.append(nums)
        
        for i in numeros:
            if numeros.get(i)==1:
                return(i)