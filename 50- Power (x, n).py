class Solution:
    def myPow (self, x: float, n: int) -> float:
        temp= 1
    
        if n==0:
            return 1
    
        if n<0:
            x=1/x
            n=n*(-1)
    
        while n>1:
            if n%2==1:
                n=n-1
                temp=temp*x
            x=x*x
            n=n/2
        
        x=x*temp
    
        return x