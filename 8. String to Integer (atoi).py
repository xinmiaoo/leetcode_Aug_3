class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s=str.strip()
        if len(s)==0 or s[0] not in "0123456789-+" or s=="-" or s=="+":
            return 0
        ans=0
        if s[0]=="-":
            sign=-1
            s=s[1:]
        elif s[0]=="+":
            sign=1
            s=s[1:]
        else:
            sign=1
        for i in range(len(s)):
            if s[i].isdigit():
                ans=ans*10+ord(s[i])-ord("0")
            else:
                break
        
        ans=ans*sign
        if ans>2**31-1:
            return 2**31-1
        if ans<-2**31:
            return -2**31
        return ans
