class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
#         sign=-1 if x<0 else 1
#         ans=0
#         x=abs(x)
#         while x!=0:
#             ans=ans*10+x%10
#             x=x/10
         
#         ans=ans*sign
#         if ans>-2**31 and ans<(2**31-1):
#             return ans
#         else:
#             return 0

        
        if x<0 :
            ans=-int(str(-x)[::-1])
        else:
            ans=int(str(x)[::-1])
            
        if ans>-2**31 and ans<(2**31-1):
            return ans
        else:
            return 0
        
