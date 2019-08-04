class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d=[(1000,'M'),(900,'CM'),(500,'D'),(400,"CD"),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I'),]
        
        ans=""
        for i in range(6):
            if num>=d[2*i][0]:
                n=num/d[2*i][0]
                num=num%d[2*i][0]
                for j in range(n):
                    ans+=d[2*i][1]
            if num>=d[2*i+1][0]:
                num=num-d[2*i+1][0]
                ans+=d[2*i+1][1]
                
        for i in range(num):
            ans+="I"
                
        return ans
