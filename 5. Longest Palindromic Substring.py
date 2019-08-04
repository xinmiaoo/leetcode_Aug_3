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
