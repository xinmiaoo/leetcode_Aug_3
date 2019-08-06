class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r=0,len(nums)-1
        while l<=r:
            m=l+(r-l)/2
            if nums[m]>target:
                if nums[m]>=nums[l] and nums[l]>target:
                    l=m+1
                else:
                    r=m-1
                    
            elif nums[m]<target:
                if nums[m]<=nums[l] and nums[r]<target:
                    r=m-1
                else:
                    l=m+1
                    
            else:
                return m

        return -1
                     
