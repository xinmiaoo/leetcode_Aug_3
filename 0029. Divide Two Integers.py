class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            sign=1
        else:
            sign=-1
        
        dividend,divisor=abs(dividend),abs(divisor)
        
        ans=0
        while dividend>=divisor:
            
            multi_divisor=divisor
            count=1
            while 2*multi_divisor<=dividend:
                multi_divisor+=multi_divisor
                count+=count
            ans+=count
            dividend-=multi_divisor
            
        if ans*sign>2**31-1:
            return 2**31-1
        if ans*sign<-2**31:
            return -2**31
        return ans*sign
