import math

class Solution:
    def reverse(self, x: int) -> int:
        negative= bool
        result=0

        if x == 0 :
            return 0
        
        if x<0:
            negative=True
            x=abs(x)

        
        for i in range(0,int(math.log10(x))+1):
            result=(result*10)+x%10
            x//=10

        
        if negative==True:
            result*=-1

        if pow(-2,31) <= result <= pow(2,31) - 1:
            return result
        
        return 0