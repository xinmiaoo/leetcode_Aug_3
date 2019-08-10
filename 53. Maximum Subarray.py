class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=nums[0]
        res=dp
        if len(nums)==0:
            return res
        for i in range(1,len(nums)):
            dp=dp+nums[i] if dp>0 else nums[i]
            res=max(res,dp)
            
            
        return res
