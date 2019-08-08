class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        
        def backtrack(nums,l):
            if not nums:
                res.append(l)
                return 
            else:
                for i in range(len(nums)):
                    if i>0 and nums[i]==nums[i-1]:
                        continue
                    if i==len(nums)-1:
                        backtrack(nums[:i],l+[nums[i]])
                    else:
                        backtrack(nums[:i]+nums[i+1:],l+[nums[i]])
                        
        nums.sort()  
        backtrack(nums,[])
        return res
