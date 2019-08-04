class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        nums.sort()
        ans=sum(nums[:3])
        for i in range(n-2):
            l,r=i+1,n-1
            while l<r:
                sum3=nums[i]+nums[l]+nums[r]
                if sum3==target:
                    return target
                elif sum3<target:
                    if abs(sum3-target)<abs(ans-target):
                        ans=sum3
                    l+=1
                else:
                    if abs(sum3-target)<abs(ans-target):
                        ans=sum3
                    r-=1
                    
                    
                    
        return ans
                    
            
