class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        
        def backtrack(nums,s,l):
            if len(l)==len(nums):
                res.append(l)
                return 
            else:
                for i in range(len(nums)):
                    if i not in s:
                        backtrack(nums,s+[i],l+[nums[i]])
                    else:
                        continue
                        
        
        backtrack(nums,[],[])
        return res
