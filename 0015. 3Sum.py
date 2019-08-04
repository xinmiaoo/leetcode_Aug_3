class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        n=len(nums)
        nums.sort()
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,n-1
            nums[i]
            while(l<r):
                if nums[l]+nums[r]+nums[i]==0:
                    ans.append([nums[l],nums[r],nums[i]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif nums[l]+nums[r]+nums[i]<0:
                    l+=1
                else:
                    r-=1
                    
                    
        return ans
