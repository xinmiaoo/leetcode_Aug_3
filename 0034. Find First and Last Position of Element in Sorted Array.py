class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx1,idx2=-1,-1
        l,r=0,len(nums)-1
        while l<=r:
            mid=l+(r-l)/2
            if nums[mid]==target:
                if mid==0 or nums[mid-1]!=target:
                    idx1=mid
                    break
                else:
                    r=mid-1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        l,r=0,len(nums)-1
        while l<=r:
            mid=l+(r-l)/2
            if nums[mid]==target:
                if mid==len(nums)-1 or nums[mid+1]!=target:
                    idx2=mid
                    break
                else:
                    l=mid+1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        
        return [idx1,idx2]
