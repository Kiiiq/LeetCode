class Solution:
    def mySqrt(self, x: int) -> int:
        y=x
        if x==0:
            return 0

        for i in range(20):
            y=(y+(x/y))/2
        
        
        return int(y)