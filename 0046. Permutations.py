# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res=[]
        
#         def backtrack(nums,s,l):
#             if len(l)==len(nums):
#                 res.append(l)
#                 return 
#             else:
#                 for i in range(len(nums)):
#                     if i not in s:
#                         backtrack(nums,s+[i],l+[nums[i]])
#                     else:
#                         continue
                        
        
#         backtrack(nums,[],[])
#         return res
    
class Solution(object):
    def permute(self, nums):
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
                    if i==len(nums)-1:
                        backtrack(nums[:i],l+[nums[i]])
                    else:
                        backtrack(nums[:i]+nums[i+1:],l+[nums[i]])
                        
                        
        backtrack(nums,[])
        return res
