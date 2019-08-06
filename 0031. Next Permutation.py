class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return 
        pt=len(nums)-2
        for i in range(len(nums)-1):
            if nums[pt]<nums[pt+1]:
                pt2=len(nums)-1
                while 1:
                    if nums[pt2]>nums[pt]:
                        nums[:]=nums[:pt]+[nums[pt2]]+nums[pt2+1:][::-1]+\
                                [nums[pt]]+nums[pt+1:pt2][::-1]
                        return
                    pt2-=1
            pt-=1
            
        nums[:]=nums[::-1]
        return 
        
