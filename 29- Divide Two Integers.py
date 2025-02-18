class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        multiplied=1
        quotient=0
        negative=False
    
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            negative=True
    
        dividend= abs(dividend)
        divisor= abs(divisor)
        divisorm=divisor

        while(dividend>=divisor):
            if divisorm>dividend:
                divisorm=divisor
                multiplied=1
            dividend=dividend-divisorm
            quotient=quotient+multiplied
            divisorm=divisorm+divisorm
            multiplied=multiplied+multiplied
    
        if negative==True:
            quotient=quotient*(-1)
        
        if quotient>2147483647:
            return 2147483647
        
        if quotient<-2147483648:
            return -2147483648

        return quotient 