class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        
        sign=1 if n<0 else 0

        n=abs(n)
        res=1
        while n:
            ans=x
            times=1
            while n>=times:

                times+=times
                if times>n:
                    times/=2
                    n=n-times
                    res*=ans
                    break
                ans=ans*ans
        if sign:
            res=1/res
        if res<-2**31:
            return -2**31
        if res>2**31-1:
            return 2**31-1
        return res

            
