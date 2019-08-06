class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        l=["" for i in range(numRows)]
        up=False
        down=True
        k=0
        for i in s:
            l[k]+=i
            if down:
                k=k+1
                if k==numRows-1:
                    up=True
                    down=False 
            else:
                k=k-1
                if k==0:
                    up=False
                    down=True
                    
        ans=""   
        for i in l:
            ans+=i
            
        return ans
