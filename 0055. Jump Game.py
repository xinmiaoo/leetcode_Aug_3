class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<=1:
            return True
        
        res=nums[0]
        for i in range(1,len(nums)):
            if res<=0:
                return False
            else:
                res=max(nums[i],res-1)
        
        
        return True
