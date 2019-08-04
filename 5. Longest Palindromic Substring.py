class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
#         if len(s)<2:
#             return s 

#         n=len(s)
#         dp=[[0 for i in range(n)] for j in range(n)]
#         start=0
#         max_length=1
#         for i in range(n):
#             dp[i][i]=1
#         for i in range(n-1):
#             if s[i]==s[i+1]:
#                 dp[i][i+1]=1
#                 start=i
#                 max_length=2
#         for k in range(2,n):
#             for i in range(n-k):
#                 if dp[i+1][i+k-1]==1 and s[i]==s[i+k]:
#                     dp[i][i+k]=1
#                     start=i
#                     max_length=k+1
                    
#         return s[start:start+max_length]
        if len(s)<2:
            return s

        if s[0]==s[1]:
            rt_l,rt_r=0,1
        else:    
            rt_l,rt_r=0,0
        

        for i in range(len(s)-1):
            l,r=self.check(s,i,i)
            if r-l+1>rt_r-rt_l:
                rt_l,rt_r=l,r
            l,r=self.check(s,i,i+1)
            if r-l+1>rt_r-rt_l:
                rt_l,rt_r=l,r
        return s[rt_l:rt_r+1]
    def check(self,s,l,r):
        while l>=0 and r<=(len(s)-1) and s[l]==s[r]:
    
                l-=1
                r+=1
 
        return l+1,r-1
