class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l,r=0,len(nums)-1
        
        while l<=r:
            mid=l+(r-l)/2
            print mid,l,r
            if nums[mid]==target:
                return mid
            
            elif nums[mid]>target:
                if mid==0:
                    return 0
                elif nums[mid-1]<target:
                    return mid
                else:
                    r=mid-1
            else:
                if mid==len(nums)-1:
                    return mid+1
                elif nums[mid+1]>target:
                    return mid+1
                else:
                    l=mid+1
                    
