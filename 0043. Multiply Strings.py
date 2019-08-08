class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        
        def helpfuc(a,b):
            b=b[::-1]
            carry=0
            ans=0
            for i in range(len(b)):
                multi=(ord(a)-ord("0"))*(ord(b[i])-ord("0"))
                if multi+carry>9:
                    multi=multi+carry-10
                    ans=(multi)*(10**i)+ans
                    carry=1
                else:
                    ans=(multi+carry)*(10**i)+ans
                    carry=0
                
            if carry==1:
                ans=10**len(b)+ans
            return ans
        num1=num1[::-1]
        res=0
        for i in range(len(num1)):
            res+=10**i*helpfuc(num1[i],num2)
        return str(res)
